from loguru import logger
from pyzotero import zotero
from omegaconf import DictConfig, ListConfig
from .utils import glob_match
from .retriever import get_retriever_cls
from .protocol import CorpusPaper, Paper
import random
from datetime import datetime
from .reranker import get_reranker_cls
from .construct_email import render_email
from .utils import send_email
from .archive import archive_papers
from .history import exclude_previously_sent, load_history, update_history
from openai import OpenAI
from tqdm import tqdm
import re


def normalize_path_patterns(patterns: list[str] | ListConfig | None, config_key: str) -> list[str] | None:
    if patterns is None:
        return None

    if not isinstance(patterns, (list, ListConfig)):
        raise TypeError(
            f"config.zotero.{config_key} must be a list of glob patterns or null, "
            'for example ["2026/survey/**"]. Single strings are not supported.'
        )

    if any(not isinstance(pattern, str) for pattern in patterns):
        raise TypeError(f"config.zotero.{config_key} must contain only glob pattern strings.")

    return list(patterns)


def normalize_keywords(keywords: list[str] | ListConfig | None, config_key: str) -> list[str]:
    if keywords is None:
        return []

    if not isinstance(keywords, (list, ListConfig)):
        raise TypeError(
            f"config.paper_filter.{config_key} must be a list of strings or null."
        )

    if any(not isinstance(keyword, str) for keyword in keywords):
        raise TypeError(f"config.paper_filter.{config_key} must contain only strings.")

    return [keyword.strip().casefold() for keyword in keywords if keyword.strip()]


def normalize_keyword_groups(groups) -> list[dict]:
    if groups is None:
        return []
    if not isinstance(groups, (list, ListConfig)):
        raise TypeError("config.paper_filter.include_groups must be a list or null.")

    normalized = []
    for group_index, group in enumerate(groups):
        clauses = group.get("all") if hasattr(group, "get") else None
        if not isinstance(clauses, (list, ListConfig)) or not clauses:
            raise TypeError(
                f"config.paper_filter.include_groups[{group_index}].all must be a non-empty list."
            )
        normalized_clauses = []
        for clause_index, clause in enumerate(clauses):
            keywords = clause.get("any") if hasattr(clause, "get") else None
            normalized_keywords = normalize_keywords(
                keywords,
                f"include_groups[{group_index}].all[{clause_index}].any",
            )
            if not normalized_keywords:
                raise ValueError("Each include_groups any clause must contain a keyword.")
            normalized_clauses.append(normalized_keywords)
        normalized.append({"name": group.get("name", f"group-{group_index + 1}"), "all": normalized_clauses})
    return normalized


def deduplicate_papers(papers: list[Paper]) -> list[Paper]:
    deduplicated: dict[str, Paper] = {}
    for paper in papers:
        doi = (paper.doi or "").casefold().removeprefix("https://doi.org/")
        normalized_title = re.sub(r"\W+", "", paper.title.casefold())
        key = f"title:{normalized_title}" if normalized_title else f"doi:{doi}"
        if key not in deduplicated:
            deduplicated[key] = paper
            continue

        existing = deduplicated[key]
        for field in (
            "abstract", "pdf_url", "full_text", "publication_date", "doi", "journal",
            "open_access_status", "cited_by_count", "venue_type", "publication_status",
        ):
            if not getattr(existing, field) and getattr(paper, field):
                setattr(existing, field, getattr(paper, field))
        existing.categories = sorted(set((existing.categories or []) + (paper.categories or [])))
        existing.authors = existing.authors or paper.authors
    return list(deduplicated.values())


def filter_by_relevance_score(
    papers: list[Paper],
    min_score: float | None,
) -> list[Paper]:
    if min_score is None:
        return papers
    return [
        paper for paper in papers
        if paper.score is not None and paper.score >= min_score
    ]


class Executor:
    def __init__(self, config:DictConfig):
        self.config = config
        self.include_path_patterns = normalize_path_patterns(config.zotero.include_path, "include_path")
        self.ignore_path_patterns = normalize_path_patterns(config.zotero.ignore_path, "ignore_path")
        legacy_keywords = normalize_keywords(config.paper_filter.get("include_keywords"), "include_keywords")
        self.include_any = normalize_keywords(config.paper_filter.get("include_any"), "include_any")
        self.include_any = sorted(set(legacy_keywords + self.include_any))
        self.include_groups = normalize_keyword_groups(config.paper_filter.get("include_groups"))
        self.exclude_keywords = normalize_keywords(config.paper_filter.exclude_keywords, "exclude_keywords")
        self.retrievers = {
            source: get_retriever_cls(source)(config) for source in config.executor.source
        }
        self.reranker = get_reranker_cls(config.executor.reranker)(config)
        self.openai_client = OpenAI(api_key=config.llm.api.key, base_url=config.llm.api.base_url)
    def fetch_zotero_corpus(self) -> list[CorpusPaper]:
        logger.info("Fetching zotero corpus")
        zot = zotero.Zotero(self.config.zotero.user_id, 'user', self.config.zotero.api_key)
        collections = zot.everything(zot.collections())
        collections = {c['key']:c for c in collections}
        corpus = zot.everything(zot.items(itemType='conferencePaper || journalArticle || preprint'))
        corpus = [c for c in corpus if c['data']['abstractNote'] != '']
        def get_collection_path(col_key:str) -> str:
            if p := collections[col_key]['data']['parentCollection']:
                return get_collection_path(p) + '/' + collections[col_key]['data']['name']
            else:
                return collections[col_key]['data']['name']
        for c in corpus:
            paths = [get_collection_path(col) for col in c['data']['collections']]
            c['paths'] = paths
        logger.info(f"Fetched {len(corpus)} zotero papers")
        return [CorpusPaper(
            title=c['data']['title'],
            abstract=c['data']['abstractNote'],
            added_date=datetime.strptime(c['data']['dateAdded'], '%Y-%m-%dT%H:%M:%SZ'),
            paths=c['paths']
        ) for c in corpus]
    
    def filter_corpus(self, corpus:list[CorpusPaper]) -> list[CorpusPaper]:
        if self.include_path_patterns:
            logger.info(f"Selecting zotero papers matching include_path: {self.include_path_patterns}")
            corpus = [
                c for c in corpus
                if any(
                    glob_match(path, pattern)
                    for path in c.paths
                    for pattern in self.include_path_patterns
                )
            ]
        if self.ignore_path_patterns:
            logger.info(f"Excluding zotero papers matching ignore_path: {self.ignore_path_patterns}")
            corpus = [
                c for c in corpus
                if not any(
                    glob_match(path, pattern)
                    for path in c.paths
                    for pattern in self.ignore_path_patterns
                )
            ]
        if self.include_path_patterns or self.ignore_path_patterns:
            samples = random.sample(corpus, min(5, len(corpus)))
            samples = '\n'.join([c.title + ' - ' + '\n'.join(c.paths) for c in samples])
            logger.info(f"Selected {len(corpus)} zotero papers:\n{samples}\n...")
        return corpus

    def filter_papers(self, papers: list[Paper]) -> list[Paper]:
        if not self.include_any and not self.include_groups and not self.exclude_keywords:
            return papers

        filtered = []
        for paper in papers:
            searchable_text = f"{paper.title}\n{paper.abstract}".casefold()
            if any(keyword in searchable_text for keyword in self.exclude_keywords):
                continue
            matched_keywords = [keyword for keyword in self.include_any if keyword in searchable_text]
            matched_groups = []
            for group in self.include_groups:
                clause_matches = [
                    [keyword for keyword in clause if keyword in searchable_text]
                    for clause in group["all"]
                ]
                if all(clause_matches):
                    matched_groups.append(group["name"])
                    matched_keywords.extend(
                        keyword for matches in clause_matches for keyword in matches
                    )
            if (self.include_any or self.include_groups) and not (
                matched_keywords or matched_groups
            ):
                continue
            paper.matched_keywords = sorted(set(matched_keywords + matched_groups))
            filtered.append(paper)

        logger.info(
            f"Keyword filter retained {len(filtered)} of {len(papers)} papers "
            f"(include_any={self.include_any}, groups={len(self.include_groups)}, "
            f"exclude={self.exclude_keywords})"
        )
        return filtered

    
    def run(self):
        corpus = self.fetch_zotero_corpus()
        corpus = self.filter_corpus(corpus)
        if len(corpus) == 0:
            logger.error(f"No zotero papers found. Please check your zotero settings:\n{self.config.zotero}")
            return
        all_papers = []
        for source, retriever in self.retrievers.items():
            logger.info(f"Retrieving {source} papers...")
            papers = retriever.retrieve_papers()
            if len(papers) == 0:
                logger.info(f"No {source} papers found")
                continue
            logger.info(f"Retrieved {len(papers)} {source} papers")
            all_papers.extend(papers)
        logger.info(f"Total {len(all_papers)} papers retrieved from all sources")
        before_deduplication = len(all_papers)
        all_papers = deduplicate_papers(all_papers)
        logger.info(
            f"Deduplicated papers from {before_deduplication} to {len(all_papers)}"
        )
        all_papers = self.filter_papers(all_papers)
        history_enabled = self.config.daily_history.enabled and not (
            self.config.executor.debug and self.config.daily_history.skip_when_debug
        )
        if history_enabled:
            history = load_history(self.config.daily_history.path)
            before_history_filter = len(all_papers)
            all_papers = exclude_previously_sent(all_papers, history)
            logger.info(
                f"Daily history filter retained {len(all_papers)} of "
                f"{before_history_filter} papers"
            )
        reranked_papers = []
        if len(all_papers) > 0:
            logger.info("Reranking papers...")
            reranked_papers = self.reranker.rerank(all_papers, corpus)
            min_score = self.config.executor.get("min_relevance_score")
            before_score_filter = len(reranked_papers)
            reranked_papers = filter_by_relevance_score(reranked_papers, min_score)
            if min_score is not None:
                logger.info(
                    f"Relevance score filter retained {len(reranked_papers)} of "
                    f"{before_score_filter} papers (minimum={min_score})"
                )
            reranked_papers = reranked_papers[:self.config.executor.max_paper_num]
            logger.info("Generating TLDR and affiliations...")
            for p in tqdm(reranked_papers):
                p.generate_tldr(self.openai_client, self.config.llm)
                p.generate_affiliations(self.openai_client, self.config.llm)
        elif not self.config.executor.send_empty:
            logger.info("No new papers found. No email will be sent.")
            return
        if self.config.archive.enabled:
            archive_papers(
                reranked_papers,
                output_root=self.config.archive.output_dir,
                download_pdfs=self.config.archive.download_pdfs,
            )
        logger.info("Sending email...")
        email_content = render_email(reranked_papers)
        send_email(self.config, email_content)
        if history_enabled and reranked_papers:
            update_history(self.config.daily_history.path, reranked_papers)
        logger.info("Email sent successfully")

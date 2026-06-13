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


class Executor:
    def __init__(self, config:DictConfig):
        self.config = config
        self.include_path_patterns = normalize_path_patterns(config.zotero.include_path, "include_path")
        self.ignore_path_patterns = normalize_path_patterns(config.zotero.ignore_path, "ignore_path")
        self.include_keywords = normalize_keywords(config.paper_filter.include_keywords, "include_keywords")
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
        if not self.include_keywords and not self.exclude_keywords:
            return papers

        filtered = []
        for paper in papers:
            searchable_text = f"{paper.title}\n{paper.abstract}".casefold()
            if any(keyword in searchable_text for keyword in self.exclude_keywords):
                continue
            matched_keywords = [
                keyword for keyword in self.include_keywords if keyword in searchable_text
            ]
            if self.include_keywords and not matched_keywords:
                continue
            paper.matched_keywords = matched_keywords
            filtered.append(paper)

        logger.info(
            f"Keyword filter retained {len(filtered)} of {len(papers)} papers "
            f"(include={self.include_keywords}, exclude={self.exclude_keywords})"
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
        reranked_papers = []
        if len(all_papers) > 0:
            logger.info("Reranking papers...")
            reranked_papers = self.reranker.rerank(all_papers, corpus)
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
        logger.info("Email sent successfully")

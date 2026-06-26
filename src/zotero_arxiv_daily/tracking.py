import argparse
import os
import re
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import arxiv
import requests
from loguru import logger
from omegaconf import OmegaConf
from openai import OpenAI

from .archive import archive_papers, load_archived_papers
from .construct_email import render_email
from .history import exclude_previously_sent, load_history, paper_identity, update_history
from .openalex_search import OpenAlexSearch
from .paper_filter import filter_papers, rules_from_config
from .protocol import Paper
from .scholar_email import retrieve_scholar_email_alerts
from .utils import send_email

CONFIDENCE_RANK = {"low": 0, "medium": 1, "high": 2}
TRACKING_MODES = {"daily", "manual"}


@dataclass(frozen=True)
class TrackedResearcher:
    name: str
    aliases: tuple[str, ...]
    openalex_id: str | None = None
    semantic_scholar_id: str | None = None
    orcid: str | None = None
    groups: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()


def normalize_openalex_id(value: str | None) -> str | None:
    if not value:
        return None
    return str(value).strip().rstrip("/").rsplit("/", 1)[-1]


def normalize_author_name(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def load_tracking_config(config_path: str, tracking_config_path: str | None = None):
    config = OmegaConf.load(config_path)
    if tracking_config_path:
        tracking_path = Path(tracking_config_path)
        if tracking_path.exists():
            config = OmegaConf.merge(config, OmegaConf.load(tracking_path))
    return config


def configured_researchers(config) -> list[TrackedResearcher]:
    tracking = config.get("tracking", {}) or {}
    by_key: dict[str, TrackedResearcher] = {}

    def add(entry, groups: tuple[str, ...] = ()) -> None:
        name = str(entry.get("name", "")).strip()
        if not name:
            return
        aliases = tuple(dict.fromkeys([name] + [str(a).strip() for a in entry.get("aliases", []) or [] if str(a).strip()]))
        openalex_id = normalize_openalex_id(entry.get("openalex_id"))
        semantic_scholar_id = str(entry.get("semantic_scholar_id", "")).strip() or None
        orcid = str(entry.get("orcid", "")).strip() or None
        keywords = tuple(str(k).strip() for k in entry.get("keywords", []) or [] if str(k).strip())
        key = openalex_id or semantic_scholar_id or orcid or normalize_author_name(name)
        existing = by_key.get(key)
        merged_groups = tuple(sorted(set((existing.groups if existing else ()) + groups)))
        merged_keywords = tuple(sorted(set((existing.keywords if existing else ()) + keywords)))
        merged_aliases = tuple(dict.fromkeys((existing.aliases if existing else ()) + aliases))
        by_key[key] = TrackedResearcher(
            name=existing.name if existing else name,
            aliases=merged_aliases,
            openalex_id=openalex_id or (existing.openalex_id if existing else None),
            semantic_scholar_id=semantic_scholar_id or (existing.semantic_scholar_id if existing else None),
            orcid=orcid or (existing.orcid if existing else None),
            groups=merged_groups,
            keywords=merged_keywords,
        )

    for entry in tracking.get("researchers", []) or []:
        add(entry)
    for group in tracking.get("groups", []) or []:
        group_name = str(group.get("name", "")).strip()
        if not group_name:
            continue
        if group.get("pi"):
            pi = group.get("pi")
            if isinstance(pi, str):
                pi = {"name": pi}
            add(pi, (group_name,))
        for member in group.get("members", []) or []:
            if isinstance(member, str):
                member = {"name": member}
            add(member, (group_name,))
    return list(by_key.values())


def mark_tracking(
    paper: Paper,
    *,
    source_hit: str,
    researcher: TrackedResearcher,
    confidence: str,
    match_type: str,
) -> Paper:
    paper.source_hits = sorted(set((paper.source_hits or []) + [source_hit]))
    paper.matched_researchers = sorted(set((paper.matched_researchers or []) + [researcher.name]))
    paper.matched_groups = sorted(set((paper.matched_groups or []) + list(researcher.groups))) or None
    current = paper.tracking_confidence or "low"
    if CONFIDENCE_RANK[confidence] >= CONFIDENCE_RANK.get(current, 0):
        paper.tracking_confidence = confidence
        paper.tracking_match_type = match_type
    return paper


def merge_paper(existing: Paper, incoming: Paper) -> Paper:
    for field in (
        "abstract", "pdf_url", "full_text", "publication_date", "doi", "journal",
        "open_access_status", "cited_by_count", "venue_type", "publication_status",
    ):
        if not getattr(existing, field) and getattr(incoming, field):
            setattr(existing, field, getattr(incoming, field))
    for field in (
        "categories", "matched_keywords", "author_ids", "institution_ids", "source_hits",
        "matched_researchers", "matched_groups",
    ):
        merged = sorted(set((getattr(existing, field) or []) + (getattr(incoming, field) or [])))
        setattr(existing, field, merged or None)
    if CONFIDENCE_RANK.get(incoming.tracking_confidence or "low", 0) > CONFIDENCE_RANK.get(existing.tracking_confidence or "low", 0):
        existing.tracking_confidence = incoming.tracking_confidence
        existing.tracking_match_type = incoming.tracking_match_type
    return existing


def deduplicate_tracking_papers(papers: list[Paper]) -> list[Paper]:
    merged: dict[str, Paper] = {}
    for paper in papers:
        key = paper_identity(paper)
        if key in merged:
            merge_paper(merged[key], paper)
        else:
            merged[key] = paper
    return list(merged.values())


def date_in_range(value: str | None, from_date: str, to_date: str) -> bool:
    if not value:
        return False
    return from_date <= value[:10] <= to_date


def mode_date_range(mode: str, to_date: str | None, tracking_config) -> tuple[str, str]:
    end_date = to_date or date.today().isoformat()
    if mode == "daily":
        lookback_days = int(tracking_config.get("daily_lookback_days", 3))
    else:
        lookback_days = int(tracking_config.get("manual_lookback_days", 30))
    start_date = (date.fromisoformat(end_date) - timedelta(days=max(lookback_days - 1, 0))).isoformat()
    return start_date, end_date


def tracking_archive_name(run_date: str, mode: str) -> str:
    if mode not in TRACKING_MODES:
        raise ValueError("mode must be 'daily' or 'manual'")
    return f"{run_date}_{mode}_tracking"


def mode_history_path(tracking_config, mode: str) -> str:
    if mode == "daily":
        return str(tracking_config.get("daily_history_path", "papers/tracking/daily_history.json"))
    return str(tracking_config.get("manual_history_path", "papers/tracking/manual_history.json"))


def history_enabled_for_mode(tracking_config, mode: str) -> bool:
    if mode == "daily":
        return bool(tracking_config.get("daily_history_enabled", True))
    return bool(tracking_config.get("manual_history_enabled", False))


def retrieve_openalex(
    client: OpenAlexSearch,
    researchers: list[TrackedResearcher],
    from_date: str,
    to_date: str,
    max_results_per_researcher: int,
) -> list[Paper]:
    papers: list[Paper] = []
    for researcher in researchers:
        if not researcher.openalex_id:
            continue
        cursor = "*"
        seen = 0
        while cursor and seen < max_results_per_researcher:
            data = client._get(
                "works",
                {
                    "filter": ",".join([
                        f"authorships.author.id:{researcher.openalex_id}",
                        f"from_publication_date:{from_date}",
                        f"to_publication_date:{to_date}",
                    ]),
                    "sort": "publication_date:desc",
                    "per-page": min(100, max_results_per_researcher - seen),
                    "cursor": cursor,
                },
            )
            results = data.get("results", [])
            seen += len(results)
            for work in results:
                paper = OpenAlexSearch._to_paper(work)
                mark_tracking(
                    paper,
                    source_hit="openalex",
                    researcher=researcher,
                    confidence="high",
                    match_type="openalex_author_id",
                )
                papers.append(paper)
            cursor = (data.get("meta") or {}).get("next_cursor")
    return papers


def semantic_scholar_headers(api_key: str | None) -> dict[str, str]:
    return {"x-api-key": api_key} if api_key else {}


def retrieve_semantic_scholar(
    researchers: list[TrackedResearcher],
    from_date: str,
    to_date: str,
    max_results_per_researcher: int,
    api_key: str | None,
) -> list[Paper]:
    papers: list[Paper] = []
    fields = "paperId,title,abstract,authors,year,publicationDate,url,venue,externalIds,openAccessPdf,citationCount"
    for researcher in researchers:
        if not researcher.semantic_scholar_id:
            continue
        url = f"https://api.semanticscholar.org/graph/v1/author/{researcher.semantic_scholar_id}/papers"
        response = requests.get(
            url,
            params={"fields": fields, "limit": min(100, max_results_per_researcher)},
            headers=semantic_scholar_headers(api_key),
            timeout=60,
        )
        response.raise_for_status()
        for item in response.json().get("data", []):
            publication_date = item.get("publicationDate") or (str(item.get("year")) if item.get("year") else None)
            if not date_in_range(publication_date, from_date, to_date):
                continue
            external_ids = item.get("externalIds") or {}
            doi = external_ids.get("DOI")
            paper = Paper(
                source="semantic_scholar",
                title=item.get("title") or "Untitled",
                authors=[a.get("name", "") for a in item.get("authors", []) if a.get("name")],
                abstract=item.get("abstract") or "",
                url=item.get("url") or f"https://www.semanticscholar.org/paper/{item.get('paperId')}",
                pdf_url=(item.get("openAccessPdf") or {}).get("url"),
                publication_date=publication_date,
                doi=f"https://doi.org/{doi}" if doi and not str(doi).startswith("http") else doi,
                journal=item.get("venue"),
                cited_by_count=item.get("citationCount"),
                publication_status="published",
                author_ids=[a.get("authorId") for a in item.get("authors", []) if a.get("authorId")],
            )
            mark_tracking(
                paper,
                source_hit="semantic_scholar",
                researcher=researcher,
                confidence="high",
                match_type="semantic_scholar_author_id",
            )
            papers.append(paper)
    return papers


def retrieve_arxiv(
    researchers: list[TrackedResearcher],
    from_date: str,
    to_date: str,
    max_results_per_researcher: int,
) -> list[Paper]:
    papers: list[Paper] = []
    client = arxiv.Client(num_retries=3, delay_seconds=5)
    for researcher in researchers:
        for alias in researcher.aliases:
            search = arxiv.Search(
                query=f'au:"{alias}"',
                max_results=max_results_per_researcher,
                sort_by=arxiv.SortCriterion.SubmittedDate,
            )
            for result in client.results(search):
                published = getattr(result, "published", None)
                publication_date = published.date().isoformat() if published else None
                if not date_in_range(publication_date, from_date, to_date):
                    continue
                paper = Paper(
                    source="arxiv",
                    title=result.title,
                    authors=[a.name for a in result.authors],
                    abstract=result.summary,
                    url=result.entry_id,
                    pdf_url=result.pdf_url,
                    publication_date=publication_date,
                    doi=getattr(result, "doi", None),
                    journal=getattr(result, "journal_ref", None),
                    categories=list(getattr(result, "categories", []) or []),
                    open_access_status="open",
                    venue_type="preprint",
                    publication_status="preprint",
                )
                mark_tracking(
                    paper,
                    source_hit="arxiv",
                    researcher=researcher,
                    confidence="medium",
                    match_type="author_alias",
                )
                papers.append(paper)
    return papers


def retrieve_biorxiv(
    researchers: list[TrackedResearcher],
    from_date: str,
    to_date: str,
    max_results: int,
) -> list[Paper]:
    url = f"https://api.biorxiv.org/details/biorxiv/{from_date}/{to_date}"
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    papers: list[Paper] = []
    for item in response.json().get("collection", []):
        authors = [a.strip() for a in item.get("authors", "").split(";") if a.strip()]
        normalized_authors = {normalize_author_name(a) for a in authors}
        for researcher in researchers:
            if not any(normalize_author_name(alias) in normalized_authors for alias in researcher.aliases):
                continue
            pdf_url = f"https://www.biorxiv.org/content/{item['doi']}v{item['version']}.full.pdf"
            paper = Paper(
                source="biorxiv",
                title=item.get("title") or "Untitled",
                authors=authors,
                abstract=item.get("abstract") or "",
                url=pdf_url,
                pdf_url=pdf_url,
                publication_date=item.get("date"),
                doi=item.get("doi"),
                journal="biorxiv",
                categories=[item.get("category", "")] if item.get("category") else [],
                open_access_status="open",
                venue_type="preprint",
                publication_status="preprint",
            )
            mark_tracking(
                paper,
                source_hit="biorxiv",
                researcher=researcher,
                confidence="medium",
                match_type="author_alias",
            )
            papers.append(paper)
            if len(papers) >= max_results:
                return papers
    return papers


def write_tracking_summaries(
    papers: list[Paper],
    output: Path,
    run_date: str,
    mode: str,
    min_confidence: str,
) -> None:
    min_rank = CONFIDENCE_RANK[min_confidence]
    focused = [
        paper for paper in papers
        if CONFIDENCE_RANK.get(paper.tracking_confidence or "low", 0) >= min_rank
    ]
    lines = [f"# Researcher Tracking - {run_date} ({mode})", ""]
    lines.extend([f"Total new tracked papers: {len(papers)}", f"Highlighted papers: {len(focused)}", ""])
    if not focused:
        lines.extend(["No highlighted papers found.", ""])
    for index, paper in enumerate(focused, start=1):
        lines.extend([
            f"## {index}. {paper.title}",
            "",
            f"- Authors: {', '.join(paper.authors) or 'Unknown'}",
            f"- Source hits: {', '.join(paper.source_hits or []) or 'N/A'}",
            f"- Matched researchers: {', '.join(paper.matched_researchers or []) or 'N/A'}",
            f"- Matched groups: {', '.join(paper.matched_groups or []) or 'N/A'}",
            f"- Confidence: {paper.tracking_confidence or 'N/A'} ({paper.tracking_match_type or 'unknown'})",
            f"- Topic keywords: {', '.join(paper.matched_keywords or []) or 'N/A'}",
            f"- Journal/source: {paper.journal or paper.source}",
            f"- Publication date: {paper.publication_date or 'Unknown'}",
            f"- Article: {paper.url}",
            "",
            paper.tldr or paper.abstract or "No summary available.",
            "",
        ])
    output.write_text("\n".join(lines), encoding="utf-8")


def run_tracking(args: argparse.Namespace) -> Path:
    mode = args.mode
    if mode not in TRACKING_MODES:
        raise ValueError("--mode must be daily or manual")
    config = load_tracking_config(args.config, args.tracking_config)
    tracking = config.get("tracking", {}) or {}
    researchers = configured_researchers(config)
    if not researchers:
        logger.warning("No tracking researchers or group members configured.")

    to_date = args.to_date or date.today().isoformat()
    from_date = args.from_date or mode_date_range(mode, to_date, tracking)[0]
    max_results = int(args.max_results or tracking.get("max_results", 100))
    max_per_researcher = int(tracking.get("max_results_per_researcher", max_results))
    sources = list(tracking.get("sources", ["openalex", "semantic_scholar", "arxiv", "biorxiv", "scholar_email"]) or [])

    logger.info(f"Running {mode} tracking from {from_date} to {to_date} across {sources}")
    papers: list[Paper] = []
    openalex_key = os.environ.get("OPENALEX_API_KEY") or (config.source.openalex.get("api_key") if config.get("source") else None)
    if "openalex" in sources and any(r.openalex_id for r in researchers):
        papers.extend(retrieve_openalex(OpenAlexSearch(openalex_key), researchers, from_date, to_date, max_per_researcher))
    if "semantic_scholar" in sources:
        s2_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or tracking.get("semantic_scholar_api_key")
        papers.extend(retrieve_semantic_scholar(researchers, from_date, to_date, max_per_researcher, s2_key))
    if "arxiv" in sources:
        papers.extend(retrieve_arxiv(researchers, from_date, to_date, max_per_researcher))
    if "biorxiv" in sources:
        papers.extend(retrieve_biorxiv(researchers, from_date, to_date, max_results))
    if "scholar_email" in sources:
        papers.extend(retrieve_scholar_email_alerts(config, researchers, from_date, to_date))

    papers = deduplicate_tracking_papers(papers)
    include_any, include_groups, exclude_keywords = rules_from_config(config.paper_filter)
    topic_matched = {paper_identity(paper): paper.matched_keywords for paper in filter_papers(list(papers), include_any, include_groups, exclude_keywords)}
    for paper in papers:
        if paper_identity(paper) in topic_matched:
            paper.matched_keywords = topic_matched[paper_identity(paper)]

    history_path = mode_history_path(tracking, mode)
    if history_enabled_for_mode(tracking, mode):
        history = load_history(history_path)
        before = len(papers)
        papers = exclude_previously_sent(papers, history)
        logger.info(f"Tracking {mode} history filter retained {len(papers)} of {before} papers")

    papers.sort(key=lambda p: (CONFIDENCE_RANK.get(p.tracking_confidence or "low", 0), p.publication_date or ""), reverse=True)
    papers = papers[:max_results]

    if args.summarize and papers:
        openai_client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
            base_url=os.environ["OPENAI_API_BASE"],
        )
        llm_config = {
            "language": os.environ.get("SUMMARY_LANGUAGE", config.llm.get("language", "Chinese")),
            "generation_kwargs": {"model": os.environ.get("OPENAI_MODEL", config.llm.generation_kwargs.model)},
        }
        for paper in papers:
            paper.generate_tldr(openai_client, llm_config)

    archive_date = args.archive_date or date.today().isoformat()
    output_root = Path(args.output_dir or tracking.get("output_dir", "papers/tracking"))
    archive_dir = archive_papers(
        papers,
        output_root=output_root,
        run_date=archive_date,
        download_pdfs=not args.skip_pdf_download and bool(tracking.get("download_pdfs", True)),
        directory_name=tracking_archive_name(archive_date, mode),
    )
    archived_papers, _, _ = load_archived_papers(archive_dir / "papers.csv")
    write_tracking_summaries(
        archived_papers,
        archive_dir / "summaries.md",
        archive_date,
        mode,
        str(tracking.get("min_confidence_for_summary", "medium")),
    )
    uncertain = [paper for paper in archived_papers if paper.tracking_confidence == "low"]
    if uncertain:
        write_tracking_summaries(uncertain, archive_dir / "uncertain.md", archive_date, mode, "low")
    if history_enabled_for_mode(tracking, mode) and papers:
        update_history(history_path, papers)
    if args.send_email:
        logger.info("Sending tracking email...")
        send_email(config, render_email(papers), subject_prefix=f"Researcher Tracking {mode}")
    return archive_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Track configured researchers and groups across scholarly sources")
    parser.add_argument("--config", default="config/custom.yaml")
    parser.add_argument("--tracking-config", default="config/tracking.yaml")
    parser.add_argument("--mode", choices=("daily", "manual"), default="manual")
    parser.add_argument("--from-date", default=None)
    parser.add_argument("--to-date", default=None)
    parser.add_argument("--archive-date", default=date.today().isoformat())
    parser.add_argument("--max-results", type=int, default=None)
    parser.add_argument("--output-dir", default=None)
    parser.add_argument("--skip-pdf-download", action="store_true")
    parser.add_argument("--summarize", action="store_true")
    parser.add_argument("--send-email", action="store_true")
    args = parser.parse_args()
    archive_dir = run_tracking(args)
    print(f"Saved {args.mode} tracking results to {archive_dir}")


if __name__ == "__main__":
    main()

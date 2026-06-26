import csv
import re
from datetime import date
from pathlib import Path

import requests
from loguru import logger

from .protocol import Paper


INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')

CSV_FIELDNAMES = [
    "index", "title", "authors", "abstract", "summary", "source",
    "venue_type", "journal", "publication_status", "publication_date", "doi", "categories", "score",
    "matched_keywords", "source_hits", "matched_researchers", "matched_groups",
    "tracking_confidence", "tracking_match_type", "author_ids", "institution_ids",
    "cited_by_count", "article_url", "pdf_url", "open_access_status",
    "local_pdf", "pdf_download_status",
]


def safe_title(title: str, max_length: int = 120) -> str:
    cleaned = INVALID_FILENAME_CHARS.sub("_", title)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" ._")
    return (cleaned or "untitled")[:max_length].rstrip(" ._")


def paper_filename(run_date: str, index: int, title: str) -> str:
    return f"{run_date}_{index:02d}_{safe_title(title)}.pdf"


def split_list(value: str | None) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def normalized_title(title: str) -> str:
    return re.sub(r"\W+", "", title.casefold())


def normalized_doi(doi: str | None) -> str:
    return (doi or "").casefold().removeprefix("https://doi.org/").strip()


def paper_keys(paper: Paper) -> list[str]:
    keys = []
    doi = normalized_doi(paper.doi)
    if doi:
        keys.append(f"doi:{doi}")
    if paper.url:
        keys.append(f"url:{paper.url.strip().casefold()}")
    title_key = normalized_title(paper.title)
    if title_key:
        keys.append(f"title:{title_key}")
    return keys


def merge_values(existing, incoming):
    if existing in (None, "", []):
        return incoming
    if incoming in (None, "", []):
        return existing
    if isinstance(existing, list) and isinstance(incoming, list):
        merged = list(existing)
        seen = {item.casefold() for item in merged}
        for item in incoming:
            if item.casefold() not in seen:
                merged.append(item)
                seen.add(item.casefold())
        return merged
    return existing


def merge_paper(existing: Paper, incoming: Paper) -> Paper:
    for field in (
        "source", "title", "authors", "abstract", "url", "pdf_url", "full_text", "tldr",
        "affiliations", "score", "publication_date", "doi", "journal", "categories",
        "open_access_status", "cited_by_count", "matched_keywords", "venue_type",
        "publication_status", "author_ids", "institution_ids", "source_hits",
        "matched_researchers", "matched_groups", "tracking_confidence", "tracking_match_type",
    ):
        setattr(existing, field, merge_values(getattr(existing, field), getattr(incoming, field)))
    return existing


def paper_from_csv_row(row: dict[str, str]) -> Paper:
    score = row.get("score") or ""
    cited_by_count = row.get("cited_by_count") or ""
    return Paper(
        source=row.get("source") or "archive",
        title=row.get("title") or "",
        authors=split_list(row.get("authors")),
        abstract=row.get("abstract") or "",
        url=row.get("article_url") or "",
        pdf_url=row.get("pdf_url") or None,
        tldr=row.get("summary") or None,
        score=float(score) if score else None,
        publication_date=row.get("publication_date") or None,
        doi=row.get("doi") or None,
        journal=row.get("journal") or None,
        categories=split_list(row.get("categories")),
        open_access_status=row.get("open_access_status") or None,
        cited_by_count=int(cited_by_count) if cited_by_count else None,
        matched_keywords=split_list(row.get("matched_keywords")),
        venue_type=row.get("venue_type") or None,
        publication_status=row.get("publication_status") or None,
        author_ids=split_list(row.get("author_ids")),
        institution_ids=split_list(row.get("institution_ids")),
        source_hits=split_list(row.get("source_hits")),
        matched_researchers=split_list(row.get("matched_researchers")),
        matched_groups=split_list(row.get("matched_groups")),
        tracking_confidence=row.get("tracking_confidence") or None,
        tracking_match_type=row.get("tracking_match_type") or None,
    )


def load_archived_papers(csv_path: Path) -> tuple[list[Paper], dict[str, str], dict[str, str]]:
    if not csv_path.exists():
        return [], {}, {}
    papers = []
    pdf_names = {}
    pdf_statuses = {}
    with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            paper = paper_from_csv_row(row)
            papers.append(paper)
            key = archive_key(paper)
            if key:
                pdf_names[key] = row.get("local_pdf") or ""
                pdf_statuses[key] = row.get("pdf_download_status") or ""
    return papers, pdf_names, pdf_statuses


def archive_key(paper: Paper) -> str:
    keys = paper_keys(paper)
    return keys[0] if keys else ""


def merge_archive_papers(existing_papers: list[Paper], new_papers: list[Paper]) -> list[Paper]:
    merged = list(existing_papers)
    key_to_index = {}
    for index, paper in enumerate(merged):
        for key in paper_keys(paper):
            key_to_index[key] = index
    for paper in new_papers:
        match_index = next((key_to_index[key] for key in paper_keys(paper) if key in key_to_index), None)
        if match_index is None:
            key_to_index.update({key: len(merged) for key in paper_keys(paper)})
            merged.append(paper)
        else:
            merged[match_index] = merge_paper(merged[match_index], paper)
            for key in paper_keys(merged[match_index]):
                key_to_index[key] = match_index
    return merged


def download_pdf(url: str, destination: Path) -> bool:
    try:
        with requests.get(url, timeout=60, stream=True) as response:
            response.raise_for_status()
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        handle.write(chunk)
        return True
    except Exception as exc:
        logger.warning(f"Failed to download PDF {url}: {exc}")
        destination.unlink(missing_ok=True)
        return False


def write_papers_csv(
    papers: list[Paper],
    output: Path,
    pdf_names: dict[int, str],
    pdf_statuses: dict[int, str],
) -> None:
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=CSV_FIELDNAMES,
        )
        writer.writeheader()
        for index, paper in enumerate(papers, start=1):
            writer.writerow(
                {
                    "index": index,
                    "title": paper.title,
                    "authors": "; ".join(paper.authors),
                    "abstract": paper.abstract,
                    "summary": paper.tldr or "",
                    "source": paper.source,
                    "venue_type": paper.venue_type or "",
                    "journal": paper.journal or "",
                    "publication_status": paper.publication_status or "",
                    "publication_date": paper.publication_date or "",
                    "doi": paper.doi or "",
                    "categories": "; ".join(paper.categories or []),
                    "score": "" if paper.score is None else paper.score,
                    "matched_keywords": "; ".join(paper.matched_keywords or []),
                    "source_hits": "; ".join(paper.source_hits or []),
                    "matched_researchers": "; ".join(paper.matched_researchers or []),
                    "matched_groups": "; ".join(paper.matched_groups or []),
                    "tracking_confidence": paper.tracking_confidence or "",
                    "tracking_match_type": paper.tracking_match_type or "",
                    "author_ids": "; ".join(paper.author_ids or []),
                    "institution_ids": "; ".join(paper.institution_ids or []),
                    "cited_by_count": "" if paper.cited_by_count is None else paper.cited_by_count,
                    "article_url": paper.url,
                    "pdf_url": paper.pdf_url or "",
                    "open_access_status": paper.open_access_status or "unknown",
                    "local_pdf": pdf_names.get(index, ""),
                    "pdf_download_status": pdf_statuses.get(index, "not_attempted"),
                }
            )


def write_summaries(papers: list[Paper], output: Path, run_date: str, pdf_names: dict[int, str]) -> None:
    lines = [f"# Paper Daily Reading - {run_date}", ""]
    if not papers:
        lines.extend(["No papers found.", ""])
    for index, paper in enumerate(papers, start=1):
        lines.extend(
            [
                f"## {index}. {paper.title}",
                "",
                f"- Authors: {', '.join(paper.authors) or 'Unknown'}",
                f"- Source: {paper.source}",
                f"- Venue type: {paper.venue_type or 'Unknown'}",
                f"- Journal: {paper.journal or 'Unknown'}",
                f"- Publication status: {paper.publication_status or 'Unknown'}",
                f"- Publication date: {paper.publication_date or 'Unknown'}",
                f"- DOI: {paper.doi or 'Unavailable'}",
                f"- Categories: {', '.join(paper.categories or []) or 'Unknown'}",
                f"- Relevance: {paper.score if paper.score is not None else 'Unknown'}",
                f"- Tracking confidence: {paper.tracking_confidence or 'N/A'}",
                f"- Source hits: {', '.join(paper.source_hits or []) or 'N/A'}",
                f"- Matched researchers: {', '.join(paper.matched_researchers or []) or 'N/A'}",
                f"- Matched groups: {', '.join(paper.matched_groups or []) or 'N/A'}",
                f"- Article: {paper.url}",
                f"- PDF: {paper.pdf_url or 'Unavailable'}",
                f"- Local PDF: {pdf_names.get(index, 'Not downloaded')}",
                "",
                paper.tldr or paper.abstract or "No summary available.",
                "",
            ]
        )
    output.write_text("\n".join(lines), encoding="utf-8")


def archive_papers(
    papers: list[Paper],
    output_root: str | Path = ".",
    run_date: str | None = None,
    download_pdfs: bool = True,
    directory_name: str | None = None,
) -> Path:
    archive_date = run_date or date.today().isoformat()
    archive_dir = Path(output_root) / (directory_name or archive_date)
    pdf_dir = archive_dir / "pdf"
    archive_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(exist_ok=True)

    existing_papers, existing_pdf_names, existing_pdf_statuses = load_archived_papers(
        archive_dir / "papers.csv"
    )
    papers = merge_archive_papers(existing_papers, papers)

    pdf_names = {}
    pdf_statuses = {}
    if download_pdfs:
        for index, paper in enumerate(papers, start=1):
            key = archive_key(paper)
            existing_pdf = existing_pdf_names.get(key, "")
            if existing_pdf:
                pdf_names[index] = existing_pdf
                existing_path = archive_dir / existing_pdf
                if existing_path.exists():
                    pdf_statuses[index] = existing_pdf_statuses.get(key) or "downloaded"
                    continue
            if not paper.pdf_url:
                pdf_statuses[index] = existing_pdf_statuses.get(key) or "no_pdf_url"
                continue
            filename = Path(existing_pdf).name if existing_pdf else paper_filename(archive_date, index, paper.title)
            if download_pdf(paper.pdf_url, pdf_dir / filename):
                pdf_names[index] = f"pdf/{filename}"
                pdf_statuses[index] = "downloaded"
            else:
                pdf_statuses[index] = existing_pdf_statuses.get(key) or "failed"
    else:
        for index, paper in enumerate(papers, start=1):
            key = archive_key(paper)
            if existing_pdf_names.get(key):
                pdf_names[index] = existing_pdf_names[key]
            pdf_statuses[index] = existing_pdf_statuses.get(key) or "skipped"

    write_papers_csv(papers, archive_dir / "papers.csv", pdf_names, pdf_statuses)
    write_summaries(papers, archive_dir / "summaries.md", archive_date, pdf_names)
    logger.info(f"Archived {len(papers)} papers to {archive_dir.resolve()}")
    return archive_dir

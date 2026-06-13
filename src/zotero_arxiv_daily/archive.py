import csv
import re
from datetime import date
from pathlib import Path

import requests
from loguru import logger

from .protocol import Paper


INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def safe_title(title: str, max_length: int = 120) -> str:
    cleaned = INVALID_FILENAME_CHARS.sub("_", title)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" ._")
    return (cleaned or "untitled")[:max_length].rstrip(" ._")


def paper_filename(run_date: str, index: int, title: str) -> str:
    return f"{run_date}_{index:02d}_{safe_title(title)}.pdf"


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


def write_papers_csv(papers: list[Paper], output: Path, pdf_names: dict[int, str]) -> None:
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "index", "title", "authors", "abstract", "summary", "score",
                "source", "url", "pdf_url", "local_pdf",
            ],
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
                    "score": "" if paper.score is None else paper.score,
                    "source": paper.source,
                    "url": paper.url,
                    "pdf_url": paper.pdf_url or "",
                    "local_pdf": pdf_names.get(index, ""),
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
                f"- Relevance: {paper.score if paper.score is not None else 'Unknown'}",
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
) -> Path:
    archive_date = run_date or date.today().isoformat()
    archive_dir = Path(output_root) / archive_date
    pdf_dir = archive_dir / "pdf"
    archive_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(exist_ok=True)

    pdf_names = {}
    if download_pdfs:
        for index, paper in enumerate(papers, start=1):
            if not paper.pdf_url:
                continue
            filename = paper_filename(archive_date, index, paper.title)
            if download_pdf(paper.pdf_url, pdf_dir / filename):
                pdf_names[index] = f"pdf/{filename}"

    write_papers_csv(papers, archive_dir / "papers.csv", pdf_names)
    write_summaries(papers, archive_dir / "summaries.md", archive_date, pdf_names)
    logger.info(f"Archived {len(papers)} papers to {archive_dir.resolve()}")
    return archive_dir

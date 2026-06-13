from pathlib import Path

from zotero_arxiv_daily.archive import archive_papers, paper_filename, safe_title
from zotero_arxiv_daily.protocol import Paper


def make_paper(title="Spatial Omics: Cell/Cell Communication?"):
    return Paper(
        source="arxiv",
        title=title,
        authors=["A. Author", "B. Author"],
        abstract="Abstract text.",
        url="https://example.com/article",
        pdf_url=None,
        tldr="A short Chinese summary.",
        score=8.5,
    )


def test_safe_title_removes_windows_invalid_characters():
    assert safe_title('A: B/C? D* "E"') == "A_ B_C_ D_ _E"


def test_paper_filename_uses_date_index_and_title():
    assert paper_filename("2026-06-14", 2, "Spatial Omics") == (
        "2026-06-14_02_Spatial Omics.pdf"
    )


def test_archive_papers_creates_expected_structure(tmp_path: Path):
    archive_dir = archive_papers(
        [make_paper()],
        output_root=tmp_path,
        run_date="2026-06-14",
        download_pdfs=False,
    )

    assert archive_dir == tmp_path / "2026-06-14"
    assert (archive_dir / "papers.csv").exists()
    assert (archive_dir / "summaries.md").exists()
    assert (archive_dir / "pdf").is_dir()
    assert "Spatial Omics" in (archive_dir / "summaries.md").read_text(encoding="utf-8")

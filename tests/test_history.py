import json

from zotero_arxiv_daily.history import (
    exclude_previously_sent,
    load_history,
    paper_identities,
    paper_identity,
    update_history,
)
from zotero_arxiv_daily.protocol import Paper


def make_paper(title="Spatial Omics", doi=None):
    return Paper(
        source="openalex",
        title=title,
        authors=[],
        abstract="",
        url="https://example.com/article",
        doi=doi,
    )


def test_paper_identity_prefers_doi():
    assert paper_identity(make_paper(doi="https://doi.org/10.1000/ABC")) == "doi:10.1000/abc"
    assert paper_identities(make_paper(doi="https://doi.org/10.1000/ABC")) == [
        "doi:10.1000/abc",
        "title:spatialomics",
    ]


def test_history_filters_daily_papers_but_keeps_unseen():
    seen = make_paper("Seen Paper")
    unseen = make_paper("Unseen Paper")
    history = {paper_identity(seen): {"sent_date": "2026-06-13"}}

    assert exclude_previously_sent([seen, unseen], history) == [unseen]


def test_update_history_persists_metadata(tmp_path):
    path = tmp_path / "papers" / "daily" / "history.json"
    paper = make_paper(doi="10.1000/example")

    update_history(path, [paper], sent_date="2026-06-14")

    data = load_history(path)
    assert data["doi:10.1000/example"]["sent_date"] == "2026-06-14"
    assert data["title:spatialomics"]["sent_date"] == "2026-06-14"
    assert json.loads(path.read_text(encoding="utf-8")) == data

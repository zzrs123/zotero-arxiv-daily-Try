from omegaconf import OmegaConf

from zotero_arxiv_daily.protocol import Paper
from zotero_arxiv_daily.tracking import (
    TrackedResearcher,
    configured_researchers,
    deduplicate_tracking_papers,
    load_tracking_config,
    mark_tracking,
    mode_date_range,
    resolve_archive_date,
    tracking_archive_name,
)


def test_configured_researchers_merges_group_members_by_openalex_id():
    config = OmegaConf.create({
        "tracking": {
            "researchers": [
                {"name": "Jane Doe", "openalex_id": "https://openalex.org/A1", "aliases": ["J. Doe"]},
            ],
            "groups": [
                {
                    "name": "Doe Lab",
                    "members": [
                        {"name": "Jane Doe", "openalex_id": "A1", "keywords": ["spatial omics"]},
                    ],
                }
            ],
        }
    })

    researchers = configured_researchers(config)

    assert len(researchers) == 1
    assert researchers[0].openalex_id == "A1"
    assert researchers[0].groups == ("Doe Lab",)
    assert researchers[0].keywords == ("spatial omics",)


def test_mark_tracking_keeps_highest_confidence_and_evidence():
    researcher = TrackedResearcher(name="Jane Doe", aliases=("Jane Doe",), groups=("Doe Lab",))
    paper = Paper(source="arxiv", title="A", authors=[], abstract="", url="u")

    mark_tracking(paper, source_hit="arxiv", researcher=researcher, confidence="medium", match_type="author_alias")
    mark_tracking(paper, source_hit="openalex", researcher=researcher, confidence="high", match_type="openalex_author_id")

    assert paper.source_hits == ["arxiv", "openalex"]
    assert paper.matched_researchers == ["Jane Doe"]
    assert paper.matched_groups == ["Doe Lab"]
    assert paper.tracking_confidence == "high"
    assert paper.tracking_match_type == "openalex_author_id"


def test_deduplicate_tracking_papers_merges_source_hits_by_doi():
    first = Paper(
        source="arxiv",
        title="Same Paper",
        authors=["Jane Doe"],
        abstract="",
        url="https://arxiv.org/abs/1",
        doi="10.1/example",
        source_hits=["arxiv"],
        matched_researchers=["Jane Doe"],
        tracking_confidence="medium",
    )
    second = Paper(
        source="openalex",
        title="Same Paper",
        authors=["Jane Doe"],
        abstract="full abstract",
        url="https://doi.org/10.1/example",
        doi="https://doi.org/10.1/example",
        source_hits=["openalex"],
        matched_researchers=["Jane Doe"],
        tracking_confidence="high",
        tracking_match_type="openalex_author_id",
        author_ids=["A1"],
    )

    papers = deduplicate_tracking_papers([first, second])

    assert len(papers) == 1
    assert papers[0].abstract == "full abstract"
    assert papers[0].source_hits == ["arxiv", "openalex"]
    assert papers[0].tracking_confidence == "high"
    assert papers[0].author_ids == ["A1"]

def test_tracking_archive_name_separates_daily_and_manual():
    assert tracking_archive_name("2026-06-26", "daily") == "2026-06-26_daily_tracking"
    assert tracking_archive_name("2026-06-26", "manual") == "2026-06-26_manual_tracking"


def test_resolve_archive_date_uses_runtime_today(monkeypatch):
    class FakeDate:
        @staticmethod
        def today():
            class FakeToday:
                @staticmethod
                def isoformat():
                    return "2026-07-01"

            return FakeToday()

    monkeypatch.setattr("zotero_arxiv_daily.tracking.date", FakeDate)

    assert resolve_archive_date(None) == "2026-07-01"
    assert resolve_archive_date("2026-06-30") == "2026-06-30"


def test_mode_date_range_uses_daily_and_manual_defaults():
    tracking = OmegaConf.create({"daily_lookback_days": 3, "manual_lookback_days": 30})

    assert mode_date_range("daily", "2026-06-26", tracking) == ("2026-06-24", "2026-06-26")
    assert mode_date_range("manual", "2026-06-26", tracking) == ("2026-05-28", "2026-06-26")


def test_load_tracking_config_merges_external_tracking_yaml(tmp_path):
    base = tmp_path / "custom.yaml"
    tracking = tmp_path / "tracking.yaml"
    base.write_text("tracking:\n  researchers: []\n", encoding="utf-8")
    tracking.write_text(
        "tracking:\n  researchers:\n    - name: Jane Doe\n      openalex_id: A1\n",
        encoding="utf-8",
    )

    config = load_tracking_config(str(base), str(tracking))

    assert config.tracking.researchers[0].name == "Jane Doe"
    assert config.tracking.researchers[0].openalex_id == "A1"

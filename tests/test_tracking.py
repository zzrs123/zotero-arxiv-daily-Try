from omegaconf import OmegaConf

from zotero_arxiv_daily.protocol import Paper
from zotero_arxiv_daily.tracking import (
    TrackedResearcher,
    configured_researchers,
    deduplicate_tracking_papers,
    mark_tracking,
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
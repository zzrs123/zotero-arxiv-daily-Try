from zotero_arxiv_daily.openalex_search import (
    OpenAlexSearch,
    manual_archive_name,
    match_keywords,
    reconstruct_abstract,
    split_values,
)


def test_split_values_uses_semicolon_or_newline():
    assert split_values("spatial omics;cell communication\nagent") == [
        "spatial omics",
        "cell communication",
        "agent",
    ]


def test_reconstruct_abstract_orders_words_by_position():
    assert reconstruct_abstract({"cell": [1], "Spatial": [0], "communication": [2]}) == (
        "Spatial cell communication"
    )


def make_search_work(work_id, title, abstract_words=None, journal=None, publication_date=None):
    abstract_words = abstract_words or []
    return {
        "id": work_id,
        "display_name": title,
        "abstract_inverted_index": {
            word: [index] for index, word in enumerate(abstract_words)
        },
        "authorships": [],
        "primary_location": {
            "source": {"display_name": journal} if journal else {},
        },
        "publication_date": publication_date,
    }


def test_match_keywords_records_actual_text_matches():
    work = make_search_work(
        "W1",
        "Spatial transcriptomics method",
        ["computational", "method"],
    )

    assert match_keywords(
        work,
        ["spatial transcriptomics", "computational method", "cell communication"],
    ) == ["spatial transcriptomics", "computational method"]


def test_search_all_requires_every_keyword(monkeypatch):
    works = [
        make_search_work("W1", "Spatial transcriptomics computational method"),
        make_search_work("W2", "Spatial transcriptomics atlas"),
    ]
    client = OpenAlexSearch("fake-key")
    monkeypatch.setattr(client, "_get", lambda path, params: {"results": works})

    papers = client.search(
        ["spatial transcriptomics", "computational method"],
        [], "2026-01-01", "2026-06-15", 30, "all",
    )

    assert [paper.title for paper in papers] == [
        "Spatial transcriptomics computational method"
    ]
    assert papers[0].matched_keywords == [
        "spatial transcriptomics", "computational method"
    ]


def test_manual_archive_name_uses_default_topic():
    assert manual_archive_name("2026-06-16", "default", []) == "2026-06-16-default"


def test_manual_archive_name_summarizes_keywords_safely():
    assert manual_archive_name(
        "2026-06-16",
        "all",
        ["Spatial Transcriptomics", "cell-cell communication", "Graph/learning", "ignored"],
    ) == "2026-06-16-spatial-transcriptomics-cell-cell-communication-graph-learning"


def test_search_any_keeps_partial_matches(monkeypatch):
    works = [
        make_search_work("W1", "Spatial transcriptomics atlas"),
        make_search_work("W2", "Computational method for graphs"),
    ]
    client = OpenAlexSearch("fake-key")
    monkeypatch.setattr(client, "_get", lambda path, params: {"results": works})

    papers = client.search(
        ["spatial transcriptomics", "computational method"],
        [], "2026-01-01", "2026-06-15", 30, "any",
    )

    assert len(papers) == 2
    assert {tuple(paper.matched_keywords) for paper in papers} == {
        ("spatial transcriptomics",),
        ("computational method",),
    }


def test_search_default_uses_configured_group_rules(monkeypatch):
    works = [
        make_search_work("W1", "Spatial transcriptomics computational method"),
        make_search_work("W2", "Spatial transcriptomics clinical trial method"),
        make_search_work("W3", "Spatial transcriptomics atlas"),
    ]
    client = OpenAlexSearch("fake-key")
    monkeypatch.setattr(client, "_get", lambda path, params: {"results": works})
    rules = (
        [],
        [{
            "name": "spatial-computation",
            "all": [
                ["spatial transcriptomics"],
                ["computational", "method"],
            ],
        }],
        ["clinical trial"],
    )

    papers = client.search(
        [], [], "2026-01-01", "2026-06-15", 30, "default", rules,
    )

    assert [paper.title for paper in papers] == [
        "Spatial transcriptomics computational method"
    ]
    assert "spatial-computation" in papers[0].matched_keywords


def test_search_prefers_configured_source_order_before_date(monkeypatch):
    works = [
        make_search_work(
            "W1",
            "Entropy bioinformatics later low-priority paper",
            journal="Genome Medicine",
            publication_date="2026-06-15",
        ),
        make_search_work(
            "W2",
            "Entropy bioinformatics earlier high-priority paper",
            journal="Nature Methods",
            publication_date="2026-05-01",
        ),
        make_search_work(
            "W3",
            "Entropy bioinformatics newest high-priority paper",
            journal="Nature Methods",
            publication_date="2026-06-01",
        ),
    ]
    client = OpenAlexSearch("fake-key")
    monkeypatch.setattr(client, "_get", lambda path, params: {"results": works})

    papers = client.search(
        ["entropy", "bioinformatics"],
        [],
        "2026-01-01",
        "2026-06-15",
        30,
        "all",
        source_rank={"nature methods": 0, "genome medicine": 1},
    )

    assert [paper.title for paper in papers] == [
        "Entropy bioinformatics newest high-priority paper",
        "Entropy bioinformatics earlier high-priority paper",
        "Entropy bioinformatics later low-priority paper",
    ]


def test_to_paper_uses_open_access_pdf_and_doi():
    work = {
        "id": "https://openalex.org/W1",
        "display_name": "Spatial Omics",
        "doi": "https://doi.org/10.1/example",
        "abstract_inverted_index": {"Spatial": [0], "omics": [1]},
        "authorships": [
            {
                "author": {"display_name": "A. Author"},
                "institutions": [
                    {"display_name": "Example University"},
                    {"display_name": "Example Institute"},
                ],
            }
        ],
        "primary_location": {
            "landing_page_url": "https://journal.example/article",
            "source": {"display_name": "Nature Methods"},
        },
        "best_oa_location": {"pdf_url": "https://journal.example/article.pdf"},
        "publication_date": "2026-06-01",
        "open_access": {"is_oa": True, "oa_status": "gold"},
        "cited_by_count": 12,
        "topics": [{"display_name": "Spatial Transcriptomics"}],
    }

    paper = OpenAlexSearch._to_paper(work)

    assert paper.title == "Spatial Omics"
    assert paper.abstract == "Spatial omics"
    assert paper.authors == ["A. Author"]
    assert paper.affiliations == ["Example University", "Example Institute"]
    assert paper.url == "https://doi.org/10.1/example"
    assert paper.pdf_url == "https://journal.example/article.pdf"
    assert paper.journal == "Nature Methods"
    assert paper.publication_date == "2026-06-01"
    assert paper.open_access_status == "gold"
    assert paper.cited_by_count == 12

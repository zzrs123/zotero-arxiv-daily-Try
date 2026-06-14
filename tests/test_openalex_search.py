from zotero_arxiv_daily.openalex_search import OpenAlexSearch, reconstruct_abstract, split_values


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

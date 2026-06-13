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
        "authorships": [{"author": {"display_name": "A. Author"}}],
        "primary_location": {"landing_page_url": "https://journal.example/article"},
        "best_oa_location": {"pdf_url": "https://journal.example/article.pdf"},
    }

    paper = OpenAlexSearch._to_paper(work)

    assert paper.title == "Spatial Omics"
    assert paper.abstract == "Spatial omics"
    assert paper.authors == ["A. Author"]
    assert paper.url == "https://doi.org/10.1/example"
    assert paper.pdf_url == "https://journal.example/article.pdf"

from omegaconf import open_dict

from zotero_arxiv_daily.retriever.openalex_retriever import OpenAlexRetriever


def make_work(source_id="S1", source_name="Nature Methods"):
    return {
        "id": "https://openalex.org/W1",
        "display_name": "Spatial Omics Method",
        "doi": "https://doi.org/10.1000/example",
        "publication_date": "2026-06-13",
        "abstract_inverted_index": {"Spatial": [0], "omics": [1]},
        "authorships": [{"author": {"display_name": "A. Author"}}],
        "primary_location": {
            "landing_page_url": "https://example.com/article",
            "source": {
                "id": f"https://openalex.org/{source_id}",
                "display_name": source_name,
            },
        },
        "best_oa_location": {"pdf_url": "https://example.com/article.pdf"},
        "open_access": {"is_oa": True, "oa_status": "gold"},
        "topics": [{"display_name": "Spatial Transcriptomics"}],
        "cited_by_count": 5,
    }


def test_openalex_retriever_labels_formal_conference_publications(config, monkeypatch):
    with open_dict(config):
        config.source.openalex.api_key = "fake-key"
        config.source.openalex.journals = ["Nature Methods"]
        config.source.openalex.conferences = ["International Conference on Machine Learning"]
        config.source.openalex.lookback_days = 3
        config.source.openalex.max_results = 30

    def resolve_journals(self, names):
        return ["S1"] if names == ["Nature Methods"] else ["S2"]

    calls = []

    def get(self, path, params):
        calls.append((path, params))
        return {"results": [make_work("S2", "International Conference on Machine Learning")], "meta": {}}

    monkeypatch.setattr("zotero_arxiv_daily.openalex_search.OpenAlexSearch.resolve_journals", resolve_journals)
    monkeypatch.setattr("zotero_arxiv_daily.openalex_search.OpenAlexSearch._get", get)

    retriever = OpenAlexRetriever(config)
    papers = retriever.retrieve_papers()

    assert len(papers) == 1
    assert papers[0].venue_type == "conference"
    assert papers[0].publication_status == "formally_published"
    assert papers[0].journal == "International Conference on Machine Learning"
    assert "type:article" in calls[0][1]["filter"]

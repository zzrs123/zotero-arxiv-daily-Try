from zotero_arxiv_daily.tracking_csv import (
    clean_alert_name,
    extract_orcid,
    researcher_from_row,
    researchers_from_csv,
)


def test_clean_alert_name_removes_suffix_and_orcid():
    assert clean_alert_name("Jane Doe (ORCID: 0000-0000-0000-000X) - 新文章") == "Jane Doe"


def test_extract_orcid_from_alert_title():
    assert extract_orcid("Jane Doe (ORCID: 0000-0003-4007-9406) - 新文章") == "0000-0003-4007-9406"


def test_researcher_from_row_skips_low_by_default():
    row = {
        "original_alert_title": "Jane Doe - 新文章",
        "normalized_name": "Jane Doe",
        "topic_hint": "spatial omics; bioinformatics",
        "confidence": "low",
        "needs_review": "yes",
        "notes": "ambiguous",
        "group": "bioinfo",
    }

    assert researcher_from_row(row, include_low=False) is None
    researcher = researcher_from_row(row, include_low=True)
    assert researcher["name"] == "Jane Doe"
    assert researcher["keywords"] == ["spatial omics", "bioinformatics"]


def test_researchers_from_csv_deduplicates_names(tmp_path):
    csv_path = tmp_path / "following.csv"
    csv_path.write_text(
        "original_alert_title,normalized_name,group,topic_hint,confidence,needs_review,notes\n"
        "Jane Doe - 新文章,Jane Doe,bio,spatial omics,high,no,ok\n"
        "Jane Doe - 新文章,Jane Doe,bio,spatial omics,high,no,dup\n"
        "Low Person - 新文章,Low Person,bio,omics,low,yes,skip\n",
        encoding="utf-8",
    )

    researchers = researchers_from_csv(csv_path)

    assert [item["name"] for item in researchers] == ["Jane Doe"]
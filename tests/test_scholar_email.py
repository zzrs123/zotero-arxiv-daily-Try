from zotero_arxiv_daily.scholar_email import (
    alert_matches_researcher,
    alert_to_paper,
    parse_alert_message,
)
from zotero_arxiv_daily.tracking import TrackedResearcher


def make_raw_alert() -> bytes:
    return (
        "From: Google Scholar Alerts <scholaralerts-noreply@google.com>\n"
        "Subject: Jane Doe - new articles\n"
        "Date: Thu, 25 Jun 2026 12:00:00 +0000\n"
        "Message-ID: <alert-1@example.com>\n"
        "Content-Type: text/plain; charset=utf-8\n"
        "\n"
        "Title: Spatial transcriptomics with graph learning\n"
        "Authors: Jane Doe; Other Author\n"
        "https://example.org/paper\n"
    ).encode("utf-8")


def test_parse_alert_message_extracts_title_authors_and_url():
    alert = parse_alert_message(make_raw_alert())

    assert alert is not None
    assert alert.title == "Spatial transcriptomics with graph learning"
    assert alert.authors == ["Jane Doe", "Other Author"]
    assert alert.url == "https://example.org/paper"
    assert alert.received_date == "2026-06-25"


def test_alert_matches_only_configured_researcher_aliases():
    alert = parse_alert_message(make_raw_alert())
    tracked = TrackedResearcher(name="Jane Doe", aliases=("J. Doe",))
    untracked = TrackedResearcher(name="Someone Else", aliases=("S. Else",))

    assert alert_matches_researcher(alert, tracked)
    assert not alert_matches_researcher(alert, untracked)


def test_alert_to_paper_marks_scholar_email_source():
    alert = parse_alert_message(make_raw_alert())
    researcher = TrackedResearcher(name="Jane Doe", aliases=("Jane Doe",), groups=("Doe Lab",))

    paper = alert_to_paper(alert, researcher)

    assert paper.source == "scholar_email"
    assert paper.source_hits == ["scholar_email"]
    assert paper.matched_researchers == ["Jane Doe"]
    assert paper.matched_groups == ["Doe Lab"]
    assert paper.tracking_match_type == "scholar_alert_email"
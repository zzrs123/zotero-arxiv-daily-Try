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

def test_retrieve_scholar_email_falls_back_to_sender_credentials(monkeypatch):
    from omegaconf import OmegaConf
    from zotero_arxiv_daily import scholar_email

    captured = {}

    class FakeImap:
        def __init__(self, host, port):
            captured["host"] = host
            captured["port"] = port

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def login(self, username, password):
            captured["username"] = username
            captured["password"] = password

        def select(self, mailbox, readonly=True):
            return "NO", []

    monkeypatch.setattr(scholar_email.imaplib, "IMAP4_SSL", FakeImap)
    config = OmegaConf.create({
        "email": {"sender": "sender@gmail.com", "sender_password": "app-password"},
        "tracking": {"scholar_email": {"enabled": True, "mailbox": "Papers/Google Scholar Alerts"}},
    })

    papers = scholar_email.retrieve_scholar_email_alerts(config, [], "2026-06-01", "2026-06-26")

    assert papers == []
    assert captured["username"] == "sender@gmail.com"
    assert captured["password"] == "app-password"
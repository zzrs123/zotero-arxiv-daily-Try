import email
import email.header
import imaplib
import re
from dataclasses import dataclass
from datetime import datetime
from email.message import Message
from email.utils import parsedate_to_datetime
from html import unescape
from typing import Iterable

from loguru import logger

from .protocol import Paper

GOOGLE_SCHOLAR_MARKERS = ("scholar.google", "google scholar", "scholar alerts")
TITLE_PATTERNS = (
    re.compile(r"^\s*Title:\s*(.+)$", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*标题[:：]\s*(.+)$", re.IGNORECASE | re.MULTILINE),
)
AUTHOR_PATTERNS = (
    re.compile(r"^\s*Authors?:\s*(.+)$", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*作者[:：]\s*(.+)$", re.IGNORECASE | re.MULTILINE),
)
LINK_PATTERN = re.compile(r"https?://[^\s<>'\"]+")
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")
WHITESPACE_PATTERN = re.compile(r"\s+")


@dataclass(frozen=True)
class ScholarEmailAlert:
    title: str
    authors: list[str]
    url: str
    received_date: str | None
    message_id: str | None


def config_get(config, key: str, default=None):
    if hasattr(config, "get"):
        value = config.get(key)
        if value is not None:
            return value
    return getattr(config, key, default)


def normalize_author_name(value: str) -> str:
    return WHITESPACE_PATTERN.sub(" ", value.casefold()).strip().strip(".,;:")


def decode_header_value(value: str | None) -> str:
    if not value:
        return ""
    return str(email.header.make_header(email.header.decode_header(value)))


def message_text(message: Message) -> str:
    parts: list[str] = []
    payload: Iterable[Message] = message.walk() if message.is_multipart() else [message]
    for part in payload:
        content_type = part.get_content_type()
        if content_type not in {"text/plain", "text/html"}:
            continue
        try:
            text = part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8", errors="replace")
        except Exception:
            continue
        if content_type == "text/html":
            text = HTML_TAG_PATTERN.sub("\n", text)
            text = unescape(text)
        parts.append(text)
    return "\n".join(parts)


def first_match(patterns: tuple[re.Pattern, ...], text: str) -> str | None:
    for pattern in patterns:
        match = pattern.search(text)
        if match:
            return WHITESPACE_PATTERN.sub(" ", match.group(1)).strip()
    return None


def extract_links(text: str) -> list[str]:
    links: list[str] = []
    for link in LINK_PATTERN.findall(text):
        clean = link.rstrip(").,;]")
        if clean not in links:
            links.append(clean)
    return links


def parse_authors(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in re.split(r";|,\s+(?=[A-Z][A-Za-z .'-]+(?:$|,|;))", value) if item.strip()]


def likely_scholar_message(message: Message, text: str) -> bool:
    sender = decode_header_value(message.get("From")).casefold()
    subject = decode_header_value(message.get("Subject")).casefold()
    combined = f"{sender}\n{subject}\n{text[:1000]}".casefold()
    return any(marker in combined for marker in GOOGLE_SCHOLAR_MARKERS)


def parse_alert_message(raw: bytes) -> ScholarEmailAlert | None:
    message = email.message_from_bytes(raw)
    text = message_text(message)
    if not likely_scholar_message(message, text):
        return None
    title = first_match(TITLE_PATTERNS, text)
    if not title:
        subject = decode_header_value(message.get("Subject"))
        title = subject.replace("新文章", "").replace("new articles", "").strip(" -:")
    authors = parse_authors(first_match(AUTHOR_PATTERNS, text))
    links = extract_links(text)
    article_url = next((link for link in links if "scholar.google" not in link.casefold()), links[0] if links else "")
    received_date = None
    try:
        if message.get("Date"):
            received_date = parsedate_to_datetime(message.get("Date")).date().isoformat()
    except Exception:
        received_date = None
    if not title:
        return None
    return ScholarEmailAlert(
        title=title,
        authors=authors,
        url=article_url,
        received_date=received_date,
        message_id=message.get("Message-ID"),
    )


def alert_matches_researcher(alert: ScholarEmailAlert, researcher) -> bool:
    aliases = [researcher.name] + list(researcher.aliases or [])
    normalized_aliases = {normalize_author_name(alias) for alias in aliases if alias}
    normalized_authors = {normalize_author_name(author) for author in alert.authors if author}
    if normalized_authors and normalized_aliases.intersection(normalized_authors):
        return True
    title_text = normalize_author_name(alert.title)
    return any(alias and alias in title_text for alias in normalized_aliases)


def alert_to_paper(alert: ScholarEmailAlert, researcher) -> Paper:
    return Paper(
        source="scholar_email",
        title=alert.title,
        authors=alert.authors or [researcher.name],
        abstract="",
        url=alert.url or alert.message_id or alert.title,
        publication_date=alert.received_date,
        journal="Google Scholar Alert",
        publication_status="alert",
        source_hits=["scholar_email"],
        matched_researchers=[researcher.name],
        matched_groups=sorted(set(researcher.groups)) or None,
        tracking_confidence="medium",
        tracking_match_type="scholar_alert_email",
    )


def date_search_since(from_date: str) -> str:
    return datetime.strptime(from_date, "%Y-%m-%d").strftime("%d-%b-%Y")


def _select_mailbox(client: imaplib.IMAP4_SSL, mailbox: str) -> bool:
    for candidate in (f'"{mailbox}"', mailbox):
        status, _ = client.select(candidate, readonly=True)
        if status == "OK":
            return True
    return False


def retrieve_scholar_email_alerts(config, researchers, from_date: str, to_date: str) -> list[Paper]:
    email_cfg = (config.get("tracking", {}) or {}).get("scholar_email", {}) or {}
    if not email_cfg.get("enabled", False):
        return []
    host = str(email_cfg.get("imap_server", "imap.gmail.com"))
    port = int(email_cfg.get("imap_port", 993))
    email_config = config_get(config, "email", {}) or {}
    username = str(email_cfg.get("username") or config_get(email_config, "sender", "") or "")
    password = str(email_cfg.get("password") or config_get(email_config, "sender_password", "") or "")
    mailbox = str(email_cfg.get("mailbox", "Papers/Google Scholar Alerts"))
    if not username or not password:
        logger.warning("Scholar email import is enabled but IMAP username/password is missing. Set SCHOLAR_IMAP_* or reuse SENDER/SENDER_PASSWORD.")
        return []

    logger.info(f"Reading Scholar alert emails from IMAP mailbox/label: {mailbox}")
    papers: list[Paper] = []
    with imaplib.IMAP4_SSL(host, port) as client:
        client.login(username, password)
        if not _select_mailbox(client, mailbox):
            logger.warning(f"IMAP mailbox/label not found: {mailbox}")
            return []
        status, data = client.search(None, "SINCE", date_search_since(from_date))
        if status != "OK" or not data:
            return []
        for message_id in data[0].split():
            status, payload = client.fetch(message_id, "(RFC822)")
            if status != "OK" or not payload:
                continue
            raw = payload[0][1]
            if not isinstance(raw, bytes):
                continue
            alert = parse_alert_message(raw)
            if alert is None:
                continue
            if alert.received_date and not (from_date <= alert.received_date <= to_date):
                continue
            for researcher in researchers:
                if alert_matches_researcher(alert, researcher):
                    papers.append(alert_to_paper(alert, researcher))
    return papers
import html
import re
from dataclasses import dataclass
from datetime import date
from typing import Iterable
from urllib.parse import urljoin

import requests
from loguru import logger
from tqdm import tqdm

from ..protocol import Paper
from .base import BaseRetriever, register_retriever


ACL_BASE_URL = "https://aclanthology.org"
NEURIPS_BASE_URL = "https://proceedings.neurips.cc"


@dataclass
class OfficialConferencePaper:
    source: str
    title: str
    authors: list[str]
    abstract: str
    url: str
    pdf_url: str | None
    publication_date: str | None
    venue: str


def _strip_tags(value: str) -> str:
    value = re.sub(
        r"<span\s+class=acl-fixed-case>(.*?)</span>",
        r"\1",
        value,
        flags=re.IGNORECASE | re.DOTALL,
    )
    text = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def _meta_content(page: str, name: str) -> str | None:
    match = re.search(
        rf'<meta\s+name=["\']{re.escape(name)}["\']\s+content=["\'](.*?)["\']',
        page,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return html.unescape(match.group(1)).strip() if match else None


def _meta_contents(page: str, name: str) -> list[str]:
    return [
        html.unescape(match).strip()
        for match in re.findall(
            rf'<meta\s+name=["\']{re.escape(name)}["\']\s+content=["\'](.*?)["\']',
            page,
            flags=re.IGNORECASE | re.DOTALL,
        )
    ]


class OfficialConferenceRetriever(BaseRetriever):
    source_name: str

    def __init__(self, config):
        super().__init__(config)
        self.session = requests.Session()

    def retrieve_papers(self) -> list[Paper]:
        raw_papers = self._retrieve_raw_papers()
        logger.info("Processing papers...")
        papers = []
        for raw_paper in tqdm(raw_papers, total=len(raw_papers), desc="Converting papers"):
            try:
                papers.append(self.convert_to_paper(raw_paper))
            except Exception as exc:
                logger.warning(f"Skipping paper {getattr(raw_paper, 'title', raw_paper)}: {exc}")
        return papers

    def _get(self, url: str) -> str:
        response = self.session.get(url, timeout=60)
        response.raise_for_status()
        return response.text

    def _years(self) -> list[int]:
        configured = self.retriever_config.get("years")
        if configured:
            return [int(year) for year in configured]
        current_year = date.today().year
        lookback_years = int(self.retriever_config.get("lookback_years", 1))
        return list(range(current_year, current_year - lookback_years, -1))

    def _max_results(self) -> int:
        return int(self.retriever_config.get("max_results", 300))

    def _limit(self, papers: Iterable[OfficialConferencePaper]) -> list[OfficialConferencePaper]:
        max_results = self._max_results()
        limited = []
        for paper in papers:
            limited.append(paper)
            if len(limited) >= max_results:
                break
        return limited

    def convert_to_paper(self, raw_paper: OfficialConferencePaper) -> Paper:
        return Paper(
            source=self.name,
            title=raw_paper.title,
            authors=raw_paper.authors,
            abstract=raw_paper.abstract,
            url=raw_paper.url,
            pdf_url=raw_paper.pdf_url,
            publication_date=raw_paper.publication_date,
            journal=raw_paper.venue,
            open_access_status="open" if raw_paper.pdf_url else None,
            venue_type="conference",
            publication_status="formally_published",
        )


@register_retriever("acl_anthology")
class ACLAnthologyRetriever(OfficialConferenceRetriever):
    def _event_urls(self) -> list[tuple[str, str, int]]:
        events = list(self.retriever_config.get("events", []) or [])
        return [
            (event, f"{ACL_BASE_URL}/events/{event}-{year}/", year)
            for event in events
            for year in self._years()
        ]

    def _retrieve_raw_papers(self) -> list[OfficialConferencePaper]:
        papers = []
        for event, url, year in self._event_urls():
            try:
                page = self._get(url)
            except requests.HTTPError as exc:
                if exc.response is not None and exc.response.status_code == 404:
                    logger.info(f"ACL Anthology event not available yet: {url}")
                    continue
                raise

            papers.extend(self._parse_event_page(page, event.upper(), year))
            if len(papers) >= self._max_results():
                break
        return papers[: self._max_results()]

    def _parse_event_page(self, page: str, venue: str, year: int) -> list[OfficialConferencePaper]:
        pattern = re.compile(
            r'(<div class="d-sm-flex align-items-stretch mb-3">.*?)(?='
            r'<div class="d-sm-flex align-items-stretch mb-3">|'
            r'<div id=|'
            r'<small><a href=# class=text-muted>|'
            r'</section>)',
            flags=re.DOTALL,
        )
        papers = []
        for match in pattern.finditer(page):
            block = match.group(1)
            paper_href = re.search(r'<strong><a class=align-middle href=([^ >]+)>(.*?)</a></strong>', block, re.DOTALL)
            if not paper_href:
                continue
            title = _strip_tags(paper_href.group(2))
            if title.lower().startswith("proceedings of "):
                continue
            url = urljoin(ACL_BASE_URL, paper_href.group(1).strip('"'))
            pdf_match = re.search(r'href=(https://aclanthology\.org/[^ >]+?\.pdf)', block)
            abstract_match = re.search(r'<div class="card-body p-3 small">(.*?)</div>', block, re.DOTALL)
            authors_html = re.sub(r".*?</strong><br>", "", block, flags=re.DOTALL)
            authors_html = re.sub(r"</span>.*", "", authors_html, flags=re.DOTALL)
            authors = [
                _strip_tags(author)
                for author in re.findall(r"<a [^>]+>(.*?)</a>", authors_html, flags=re.DOTALL)
            ]
            papers.append(
                OfficialConferencePaper(
                    source=self.name,
                    title=title,
                    authors=[author for author in authors if author],
                    abstract=_strip_tags(abstract_match.group(1)) if abstract_match else "",
                    url=url,
                    pdf_url=pdf_match.group(1) if pdf_match else None,
                    publication_date=f"{year}-01-01",
                    venue=venue,
                )
            )
        return papers


@register_retriever("neurips")
class NeurIPSRetriever(OfficialConferenceRetriever):
    def _retrieve_raw_papers(self) -> list[OfficialConferencePaper]:
        papers = []
        for year in self._years():
            url = f"{NEURIPS_BASE_URL}/paper_files/paper/{year}"
            try:
                page = self._get(url)
            except requests.HTTPError as exc:
                if exc.response is not None and exc.response.status_code == 404:
                    logger.info(f"NeurIPS proceedings not available yet: {url}")
                    continue
                raise
            paper_urls = self._parse_listing_page(page)
            for paper_url in paper_urls:
                if len(papers) >= self._max_results():
                    break
                try:
                    detail_page = self._get(paper_url)
                    papers.append(self._parse_detail_page(detail_page, paper_url, year))
                except Exception as exc:
                    logger.warning(f"Skipping NeurIPS paper {paper_url}: {exc}")
            if len(papers) >= self._max_results():
                break
        return papers

    def _parse_listing_page(self, page: str) -> list[str]:
        urls = []
        for href in re.findall(r'<a title="paper title" href="([^"]+)">', page):
            urls.append(urljoin(NEURIPS_BASE_URL, href))
        return urls

    def _parse_detail_page(self, page: str, url: str, year: int) -> OfficialConferencePaper:
        title = _meta_content(page, "citation_title") or _strip_tags(
            re.search(r'<h1 class="paper-title">(.*?)</h1>', page, re.DOTALL).group(1)
        )
        authors = _meta_contents(page, "citation_author")
        abstract_match = re.search(r'<p class="paper-abstract">\s*<p>(.*?)</p>', page, re.DOTALL)
        pdf_url = _meta_content(page, "citation_pdf_url")
        publication_date = _meta_content(page, "citation_publication_date") or f"{year}-01-01"
        return OfficialConferencePaper(
            source=self.name,
            title=title,
            authors=authors,
            abstract=_strip_tags(abstract_match.group(1)) if abstract_match else "",
            url=url,
            pdf_url=pdf_url,
            publication_date=publication_date,
            venue=f"NeurIPS {year}",
        )

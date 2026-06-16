import argparse
import os
from datetime import date
from pathlib import Path

import requests
from openai import OpenAI
from omegaconf import OmegaConf

from .protocol import Paper
from .archive import archive_papers
from .paper_filter import collect_query_keywords, filter_papers, rules_from_config


OPENALEX_API = "https://api.openalex.org"


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.replace("\n", ";").split(";") if item.strip()]


def reconstruct_abstract(inverted_index: dict[str, list[int]] | None) -> str:
    if not inverted_index:
        return ""
    words = [
        (position, word)
        for word, positions in inverted_index.items()
        for position in positions
    ]
    return " ".join(word for _, word in sorted(words))


def match_keywords(work: dict, keywords: list[str]) -> list[str]:
    title = work.get("display_name") or ""
    abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
    searchable_text = f"{title}\n{abstract}".casefold()
    return [keyword for keyword in keywords if keyword.casefold() in searchable_text]


class OpenAlexSearch:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("OPENALEX_API_KEY is required")
        self.api_key = api_key
        self.session = requests.Session()

    def _get(self, path: str, params: dict) -> dict:
        response = self.session.get(
            f"{OPENALEX_API}/{path}",
            params={**params, "api_key": self.api_key},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()

    def resolve_journals(self, journals: list[str]) -> list[str]:
        source_ids = []
        for journal in journals:
            results = self._get("sources", {"search": journal, "per-page": 10})["results"]
            exact = next(
                (source for source in results if source["display_name"].casefold() == journal.casefold()),
                None,
            )
            if exact is None:
                suggestions = ", ".join(source["display_name"] for source in results[:3])
                raise ValueError(f"Journal not found: {journal}. Suggestions: {suggestions}")
            source_ids.append(exact["id"].rsplit("/", 1)[-1])
        return source_ids

    def search(
        self,
        keywords: list[str],
        journals: list[str],
        from_date: str,
        to_date: str,
        max_results: int,
        match_mode: str = "all",
        configured_rules: tuple[list[str], list[dict], list[str]] | None = None,
        source_rank: dict[str, int] | None = None,
    ) -> list[Paper]:
        if match_mode not in {"default", "all", "any"}:
            raise ValueError("match_mode must be 'default', 'all', or 'any'")
        if match_mode == "default":
            if configured_rules is None:
                raise ValueError("configured_rules are required for default match mode")
            include_any, include_groups, _ = configured_rules
            query_keywords = collect_query_keywords(include_any, include_groups)
        else:
            query_keywords = keywords
        if not query_keywords:
            raise ValueError("At least one search keyword is required")

        source_rank = source_rank or {}
        prioritize_sources = bool(source_rank and journals)
        source_ids = self.resolve_journals(journals) if journals else []
        base_filters = [
            f"from_publication_date:{from_date}",
            f"to_publication_date:{to_date}",
            "type:article",
        ]
        if prioritize_sources:
            source_filter_groups = [[source_id] for source_id in source_ids]
        elif source_ids:
            source_filter_groups = [source_ids]
        else:
            source_filter_groups = [[]]

        works_by_id = {}
        for source_group in source_filter_groups:
            filters = list(base_filters)
            if source_group:
                filters.append(f"primary_location.source.id:{'|'.join(source_group)}")
            for keyword in query_keywords:
                data = self._get(
                    "works",
                    {
                        "search": keyword,
                        "filter": ",".join(filters),
                        "sort": "publication_date:desc",
                        "per-page": 100,
                    },
                )
                for work in data["results"]:
                    works_by_id[work["id"]] = work

        papers = [self._to_paper(work) for work in works_by_id.values()]
        if match_mode == "default":
            include_any, include_groups, exclude_keywords = configured_rules
            papers = filter_papers(papers, include_any, include_groups, exclude_keywords)
        else:
            matched_papers = []
            for paper, work in zip(papers, works_by_id.values(), strict=True):
                matched = match_keywords(work, keywords)
                keep = len(matched) == len(keywords) if match_mode == "all" else bool(matched)
                if keep:
                    paper.matched_keywords = matched
                    matched_papers.append(paper)
            papers = matched_papers

        papers.sort(key=lambda paper: paper.publication_date or "", reverse=True)
        if source_rank:
            papers.sort(
                key=lambda paper: source_rank.get(
                    (paper.journal or "").casefold(),
                    len(source_rank),
                )
            )
        return papers[:max_results]

    @staticmethod
    def _to_paper(work: dict, venue_type: str | None = None) -> Paper:
        primary = work.get("primary_location") or {}
        best_oa = work.get("best_oa_location") or {}
        source = primary.get("source") or {}
        open_access = work.get("open_access") or {}
        authors = [
            authorship.get("author", {}).get("display_name", "")
            for authorship in work.get("authorships", [])
        ]
        affiliations = []
        for authorship in work.get("authorships", []):
            for institution in authorship.get("institutions", []):
                name = institution.get("display_name", "")
                if name and name not in affiliations:
                    affiliations.append(name)
        return Paper(
            source="openalex",
            title=work.get("display_name") or "Untitled",
            authors=[author for author in authors if author],
            affiliations=affiliations or None,
            abstract=reconstruct_abstract(work.get("abstract_inverted_index")),
            url=work.get("doi") or primary.get("landing_page_url") or work["id"],
            pdf_url=best_oa.get("pdf_url"),
            publication_date=work.get("publication_date"),
            doi=work.get("doi"),
            journal=source.get("display_name"),
            categories=[
                topic.get("display_name", "")
                for topic in work.get("topics", [])
                if topic.get("display_name")
            ],
            open_access_status=open_access.get("oa_status") or (
                "open" if open_access.get("is_oa") else "closed"
            ),
            cited_by_count=work.get("cited_by_count"),
            venue_type=venue_type,
            publication_status=(
                "formally_published" if venue_type == "conference" else "published"
            ),
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Search journal articles through OpenAlex")
    parser.add_argument("--keywords", default="", help="Semicolon-separated keywords for all/any mode")
    parser.add_argument(
        "--match-mode",
        choices=("default", "all", "any"),
        default="default",
        help="Use configured filters, require all keywords, or require any keyword",
    )
    parser.add_argument("--config", default="config/custom.yaml", help="Config used by default mode")
    parser.add_argument(
        "--journals",
        default="",
        help="Semicolon-separated exact source names (OR); blank uses configured priority venues",
    )
    parser.add_argument("--from-date", required=True, help="Start date, YYYY-MM-DD")
    parser.add_argument("--to-date", default=date.today().isoformat(), help="End date, YYYY-MM-DD")
    parser.add_argument("--max-results", type=int, default=30)
    parser.add_argument("--output-dir", default=".")
    parser.add_argument("--archive-date", default=date.today().isoformat())
    parser.add_argument("--skip-pdf-download", action="store_true")
    parser.add_argument("--summarize", action="store_true")
    args = parser.parse_args()

    if args.max_results < 1 or args.max_results > 100:
        parser.error("--max-results must be between 1 and 100")
    if args.from_date > args.to_date:
        parser.error("--from-date must not be after --to-date")

    keywords = split_values(args.keywords)
    configured_rules = None
    configured_venues: list[str] = []
    configured_priority_sources: list[str] = []
    custom_config = OmegaConf.load(args.config)
    if args.match_mode == "default":
        configured_rules = rules_from_config(custom_config.paper_filter)
    elif not keywords:
        parser.error("--keywords is required when --match-mode is all or any")
    openalex_cfg = custom_config.get("source", {}).get("openalex", {})
    for venue_type in ("journals", "conferences"):
        for name in openalex_cfg.get(venue_type, []) or []:
            configured_venues.append(str(name))
            configured_priority_sources.append(str(name))

    journals = split_values(args.journals)
    source_rank = None
    if not journals and configured_priority_sources:
        journals = configured_venues
        source_rank = {
            source.casefold(): rank
            for rank, source in enumerate(configured_priority_sources)
        }

    client = OpenAlexSearch(os.environ.get("OPENALEX_API_KEY", ""))
    papers = client.search(
        keywords,
        journals,
        args.from_date,
        args.to_date,
        args.max_results,
        args.match_mode,
        configured_rules,
        source_rank,
    )

    if args.summarize and papers:
        openai_client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
            base_url=os.environ["OPENAI_API_BASE"],
        )
        llm_config = {
            "language": os.environ.get("SUMMARY_LANGUAGE", "Chinese"),
            "generation_kwargs": {"model": os.environ.get("OPENAI_MODEL", "gpt-5.4")},
        }
        for paper in papers:
            paper.generate_tldr(openai_client, llm_config)

    archive_dir = archive_papers(
        papers,
        output_root=Path(args.output_dir),
        run_date=args.archive_date,
        download_pdfs=not args.skip_pdf_download,
    )
    print(f"Saved {len(papers)} papers to {archive_dir}")


if __name__ == "__main__":
    main()

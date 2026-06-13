import argparse
import os
from datetime import date
from pathlib import Path

import requests
from openai import OpenAI

from .protocol import Paper
from .archive import archive_papers


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
    ) -> list[Paper]:
        source_ids = self.resolve_journals(journals) if journals else []
        filters = [
            f"from_publication_date:{from_date}",
            f"to_publication_date:{to_date}",
            "type:article",
        ]
        if source_ids:
            filters.append(f"primary_location.source.id:{'|'.join(source_ids)}")

        papers_by_id = {}
        for keyword in keywords:
            data = self._get(
                "works",
                {
                    "search": keyword,
                    "filter": ",".join(filters),
                    "sort": "publication_date:desc",
                    "per-page": min(max_results, 100),
                },
            )
            for work in data["results"]:
                if work["id"] in papers_by_id:
                    matched = papers_by_id[work["id"]].matched_keywords or []
                    if keyword not in matched:
                        matched.append(keyword)
                    papers_by_id[work["id"]].matched_keywords = matched
                else:
                    paper = self._to_paper(work)
                    paper.matched_keywords = [keyword]
                    papers_by_id[work["id"]] = paper
                if len(papers_by_id) >= max_results:
                    break
            if len(papers_by_id) >= max_results:
                break
        return list(papers_by_id.values())[:max_results]

    @staticmethod
    def _to_paper(work: dict) -> Paper:
        primary = work.get("primary_location") or {}
        best_oa = work.get("best_oa_location") or {}
        source = primary.get("source") or {}
        open_access = work.get("open_access") or {}
        authors = [
            authorship.get("author", {}).get("display_name", "")
            for authorship in work.get("authorships", [])
        ]
        return Paper(
            source="openalex",
            title=work.get("display_name") or "Untitled",
            authors=[author for author in authors if author],
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
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Search journal articles through OpenAlex")
    parser.add_argument("--keywords", required=True, help="Semicolon-separated keywords (OR)")
    parser.add_argument("--journals", default="", help="Semicolon-separated exact journal names (OR)")
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

    client = OpenAlexSearch(os.environ.get("OPENALEX_API_KEY", ""))
    papers = client.search(
        split_values(args.keywords),
        split_values(args.journals),
        args.from_date,
        args.to_date,
        args.max_results,
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

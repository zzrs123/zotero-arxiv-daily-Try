from datetime import date, timedelta
from typing import Any

from loguru import logger

from ..openalex_search import OpenAlexSearch
from ..protocol import Paper
from .base import BaseRetriever, register_retriever


@register_retriever("openalex")
class OpenAlexRetriever(BaseRetriever):
    def __init__(self, config):
        super().__init__(config)
        self.api_key = self.retriever_config.api_key
        if not self.api_key:
            raise ValueError("source.openalex.api_key or OPENALEX_API_KEY must be configured")
        self.client = OpenAlexSearch(self.api_key)
        self.venue_types: dict[str, str] = {}

    def _resolve_venues(self) -> list[str]:
        venue_ids = []
        for venue_type in ("journal", "conference"):
            names = list(self.retriever_config.get(f"{venue_type}s", []) or [])
            for name in names:
                try:
                    source_id = self.client.resolve_journals([name])[0]
                except (ValueError, IndexError) as exc:
                    logger.warning(f"Skipping unresolved OpenAlex {venue_type} {name}: {exc}")
                    continue
                venue_ids.append(source_id)
                self.venue_types[source_id] = venue_type
                logger.info(f"Resolved OpenAlex {venue_type}: {name} -> {source_id}")
        return venue_ids

    def _retrieve_raw_papers(self) -> list[dict[str, Any]]:
        venue_ids = self._resolve_venues()
        if not venue_ids:
            return []

        today = date.today()
        lookback_days = int(self.retriever_config.get("lookback_days", 3))
        filters = [
            f"from_publication_date:{(today - timedelta(days=lookback_days)).isoformat()}",
            f"to_publication_date:{today.isoformat()}",
            f"primary_location.source.id:{'|'.join(venue_ids)}",
            "type:article",
        ]
        max_results = int(self.retriever_config.get("max_results", 500))
        results = []
        cursor = "*"
        while cursor and len(results) < max_results:
            data = self.client._get(
                "works",
                {
                    "filter": ",".join(filters),
                    "sort": "publication_date:desc",
                    "per-page": min(max_results - len(results), 100),
                    "cursor": cursor,
                },
            )
            results.extend(data.get("results", []))
            cursor = (data.get("meta") or {}).get("next_cursor")
        return results[:max_results]

    def convert_to_paper(self, raw_paper: dict[str, Any]) -> Paper:
        source = (raw_paper.get("primary_location") or {}).get("source") or {}
        source_id = source.get("id", "").rsplit("/", 1)[-1]
        venue_type = self.venue_types.get(source_id)
        return OpenAlexSearch._to_paper(raw_paper, venue_type=venue_type)

import json
import re
from datetime import date
from pathlib import Path

from loguru import logger

from .protocol import Paper


def paper_identities(paper: Paper) -> list[str]:
    identities = []
    doi = (paper.doi or "").casefold().removeprefix("https://doi.org/").strip()
    if doi:
        identities.append(f"doi:{doi}")
    normalized_title = re.sub(r"\W+", "", paper.title.casefold())
    if normalized_title:
        identities.append(f"title:{normalized_title}")
    return identities


def paper_identity(paper: Paper) -> str:
    identities = paper_identities(paper)
    return identities[0] if identities else "title:"


def load_history(path: str | Path) -> dict[str, dict]:
    history_path = Path(path)
    if not history_path.exists():
        return {}
    try:
        data = json.loads(history_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning(f"Failed to read daily history {history_path}: {exc}")
        return {}
    return data if isinstance(data, dict) else {}


def exclude_previously_sent(papers: list[Paper], history: dict[str, dict]) -> list[Paper]:
    return [
        paper for paper in papers
        if not any(identity in history for identity in paper_identities(paper))
    ]


def update_history(path: str | Path, papers: list[Paper], sent_date: str | None = None) -> None:
    history_path = Path(path)
    history = load_history(history_path)
    current_date = sent_date or date.today().isoformat()
    for paper in papers:
        entry = {
            "title": paper.title,
            "doi": paper.doi,
            "url": paper.url,
            "source": paper.source,
            "sent_date": current_date,
        }
        for identity in paper_identities(paper):
            history[identity] = entry
    history_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.write_text(
        json.dumps(history, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

import argparse
import csv
import re
from pathlib import Path
from typing import Any

from omegaconf import OmegaConf

ORCID_PATTERN = re.compile(r"\b\d{4}-\d{4}-\d{4}-[\dX]{4}\b", re.IGNORECASE)


def split_keywords(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.replace("\n", ";").split(";") if item.strip()]


def clean_alert_name(value: str) -> str:
    name = re.sub(r"\s*-\s*新文章\s*$", "", value).strip()
    name = re.sub(r"\s*\(ORCID:\s*[^)]+\)", "", name, flags=re.IGNORECASE).strip()
    return name


def extract_orcid(*values: str | None) -> str | None:
    for value in values:
        if not value:
            continue
        match = ORCID_PATTERN.search(value)
        if match:
            return match.group(0)
    return None


def confidence_allowed(confidence: str, include_low: bool) -> bool:
    normalized = confidence.strip().casefold()
    return include_low or normalized in {"high", "medium", ""}


def researcher_from_row(row: dict[str, str], include_low: bool) -> dict[str, Any] | None:
    confidence = row.get("confidence", "")
    if not confidence_allowed(confidence, include_low):
        return None
    name = (row.get("normalized_name") or clean_alert_name(row.get("original_alert_title", ""))).strip()
    if not name:
        return None
    alert_name = clean_alert_name(row.get("original_alert_title", ""))
    aliases = []
    if alert_name and alert_name != name:
        aliases.append(alert_name)
    researcher: dict[str, Any] = {
        "name": name,
        "aliases": aliases,
        "keywords": split_keywords(row.get("topic_hint")),
        "source": "google_scholar_following_csv",
        "google_scholar_group": row.get("group", "").strip(),
        "classification_confidence": confidence.strip(),
        "needs_review": row.get("needs_review", "").strip(),
        "notes": row.get("notes", "").strip(),
    }
    orcid = extract_orcid(row.get("original_alert_title"), row.get("notes"))
    if orcid:
        researcher["orcid"] = orcid
    return researcher


def researchers_from_csv(input_path: str | Path, include_low: bool = False) -> list[dict[str, Any]]:
    seen = set()
    researchers = []
    with Path(input_path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            researcher = researcher_from_row(row, include_low)
            if researcher is None:
                continue
            key = researcher.get("orcid") or researcher["name"].casefold()
            if key in seen:
                continue
            seen.add(key)
            researchers.append(researcher)
    researchers.sort(key=lambda item: (item.get("google_scholar_group", ""), item["name"].casefold()))
    return researchers


def write_tracking_yaml(researchers: list[dict[str, Any]], output_path: str | Path) -> None:
    config = OmegaConf.create({"tracking": {"researchers": researchers, "groups": []}})
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        handle.write(
            "# Generated from Google Scholar following CSV.\n"
            "# Prefer adding openalex_id / semantic_scholar_id later for high-confidence tracking.\n"
        )
        OmegaConf.save(config=config, f=handle)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a Google Scholar following CSV into config/tracking.yaml")
    parser.add_argument("--input", required=True, help="CSV exported/classified from Google Scholar following alerts")
    parser.add_argument("--output", default="config/tracking.yaml", help="Tracking YAML to write")
    parser.add_argument("--include-low", action="store_true", help="Include rows whose confidence is low")
    args = parser.parse_args()

    researchers = researchers_from_csv(args.input, include_low=args.include_low)
    write_tracking_yaml(researchers, args.output)
    print(f"Wrote {len(researchers)} researchers to {args.output}")


if __name__ == "__main__":
    main()
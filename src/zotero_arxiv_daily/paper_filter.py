from omegaconf import ListConfig

from .protocol import Paper


def normalize_keywords(keywords: list[str] | ListConfig | None, config_key: str) -> list[str]:
    if keywords is None:
        return []
    if not isinstance(keywords, (list, ListConfig)):
        raise TypeError(f"config.paper_filter.{config_key} must be a list of strings or null.")
    if any(not isinstance(keyword, str) for keyword in keywords):
        raise TypeError(f"config.paper_filter.{config_key} must contain only strings.")
    return [keyword.strip().casefold() for keyword in keywords if keyword.strip()]


def normalize_keyword_groups(groups) -> list[dict]:
    if groups is None:
        return []
    if not isinstance(groups, (list, ListConfig)):
        raise TypeError("config.paper_filter.include_groups must be a list or null.")

    normalized = []
    for group_index, group in enumerate(groups):
        clauses = group.get("all") if hasattr(group, "get") else None
        if not isinstance(clauses, (list, ListConfig)) or not clauses:
            raise TypeError(
                f"config.paper_filter.include_groups[{group_index}].all must be a non-empty list."
            )
        normalized_clauses = []
        for clause_index, clause in enumerate(clauses):
            keywords = clause.get("any") if hasattr(clause, "get") else None
            normalized_keywords = normalize_keywords(
                keywords,
                f"include_groups[{group_index}].all[{clause_index}].any",
            )
            if not normalized_keywords:
                raise ValueError("Each include_groups any clause must contain a keyword.")
            normalized_clauses.append(normalized_keywords)
        normalized.append({"name": group.get("name", f"group-{group_index + 1}"), "all": normalized_clauses})
    return normalized


def rules_from_config(paper_filter_config) -> tuple[list[str], list[dict], list[str]]:
    legacy = normalize_keywords(paper_filter_config.get("include_keywords"), "include_keywords")
    include_any = normalize_keywords(paper_filter_config.get("include_any"), "include_any")
    include_any = sorted(set(legacy + include_any))
    include_groups = normalize_keyword_groups(paper_filter_config.get("include_groups"))
    exclude_keywords = normalize_keywords(paper_filter_config.get("exclude_keywords"), "exclude_keywords")
    return include_any, include_groups, exclude_keywords


def collect_query_keywords(include_any: list[str], include_groups: list[dict]) -> list[str]:
    group_keywords = [
        keyword
        for group in include_groups
        for clause in group["all"]
        for keyword in clause
    ]
    return sorted(set(include_any + group_keywords))


def filter_papers(
    papers: list[Paper],
    include_any: list[str],
    include_groups: list[dict],
    exclude_keywords: list[str],
) -> list[Paper]:
    if not include_any and not include_groups and not exclude_keywords:
        return papers

    filtered = []
    for paper in papers:
        searchable_text = f"{paper.title}\n{paper.abstract}".casefold()
        if any(keyword in searchable_text for keyword in exclude_keywords):
            continue
        matched_keywords = [keyword for keyword in include_any if keyword in searchable_text]
        matched_groups = []
        for group in include_groups:
            clause_matches = [
                [keyword for keyword in clause if keyword in searchable_text]
                for clause in group["all"]
            ]
            if all(clause_matches):
                matched_groups.append(group["name"])
                matched_keywords.extend(keyword for matches in clause_matches for keyword in matches)
        if (include_any or include_groups) and not (matched_keywords or matched_groups):
            continue
        paper.matched_keywords = sorted(set(matched_keywords + matched_groups))
        filtered.append(paper)
    return filtered

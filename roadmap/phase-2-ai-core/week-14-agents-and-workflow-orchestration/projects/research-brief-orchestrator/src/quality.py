"""Quality checks and brief drafting helpers."""

from __future__ import annotations


def draft_brief(query: str, topics: list[str], documents: list[dict[str, object]]) -> str:
    lines = [f"Research brief for: {query}", ""]

    if topics:
        lines.append(f"Topics: {', '.join(topics)}")
        lines.append("")

    if not documents:
        lines.append("Evidence: No supporting documents were found.")
        lines.append("Recommendation: Escalate for human review.")
        return "\n".join(lines)

    lines.append("Evidence summary:")
    for document in documents:
        lines.append(f"- {document['title']}: {document['summary']}")

    lines.append("")
    lines.append("Key guidance:")
    for document in documents:
        lines.append(f"- {document['details']}")

    return "\n".join(lines)


def should_request_review(topics: list[str], documents: list[dict[str, object]]) -> bool:
    if not documents:
        return True

    covered_topics = {str(document["topic"]) for document in documents}

    if "general" in topics:
        return len(documents) == 0

    return not set(topics).issubset(covered_topics)

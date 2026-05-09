"""Explain what makes one tool definition easier for a model to use well."""

from __future__ import annotations


def explain_tool_quality(name: str, description: str) -> str:
    score = 0

    if len(description.split()) >= 15:
        score += 1
    if "when" in description.lower():
        score += 1
    if "do not" in description.lower():
        score += 1
    if "parameter" in description.lower() or "input" in description.lower():
        score += 1

    if score >= 3:
        return f"{name}: strong definition"
    return f"{name}: weak definition"


def main() -> None:
    tools = [
        ("lookup_ticket", "Find ticket."),
        (
            "lookup_ticket",
            "Look up a support ticket by ID when the user needs the status, priority, owner, or summary. "
            "Use this only for ticket identifiers like T-1002. Do not use it for policy search or calculations. "
            "The input parameter is ticket_id.",
        ),
    ]

    for name, description in tools:
        print(explain_tool_quality(name, description))
        print(description)
        print()


if __name__ == "__main__":
    main()

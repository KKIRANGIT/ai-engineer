"""A simple planner that proposes tool calls from user queries.

This is intentionally rule-based so the tool loop stays easy to inspect.
"""

from __future__ import annotations

import re

from .models import ToolCall


def _extract_ticket_id(query: str) -> str | None:
    match = re.search(r"\bT-\d{4}\b", query.upper())
    return match.group(0) if match else None


def _extract_refund_arguments(query: str) -> tuple[float, float] | None:
    match = re.search(r"(\d+(?:\.\d+)?)\s*(?:percent|%)\s+of\s+(\d+(?:\.\d+)?)", query.lower())
    if not match:
        return None

    percent = float(match.group(1))
    amount = float(match.group(2))
    return amount, percent


def _extract_weather_city(query: str) -> str | None:
    match = re.search(r"(?:weather|temperature)\s+in\s+([a-zA-Z ]+)", query, re.IGNORECASE)
    if not match:
        return None

    raw_city = match.group(1)
    city = re.split(r"\b(?:and|then|for|about)\b", raw_city, maxsplit=1, flags=re.IGNORECASE)[0]
    city = city.strip(" ?.,")
    return city.title() if city else None


def _policy_query_from_text(query: str) -> tuple[str, str | None] | None:
    candidates = {
        "refund": "refund policy",
        "leave": "leave policy",
        "travel": "travel reimbursement",
        "security": "password security",
        "equipment": "equipment request",
        "laptop": "equipment request",
        "policy": "policy summary",
    }

    query_lower = query.lower()
    for keyword, search_query in candidates.items():
        if keyword in query_lower:
            topic = None if keyword == "policy" else keyword
            return search_query, topic

    return None


class RuleBasedPlanner:
    """Produce proposed tool calls from simple query patterns."""

    def plan(self, user_query: str) -> list[ToolCall]:
        calls: list[ToolCall] = []

        ticket_id = _extract_ticket_id(user_query)
        if ticket_id:
            calls.append(
                ToolCall(
                    name="lookup_ticket",
                    arguments={"ticket_id": ticket_id},
                    reason="The query includes a ticket identifier.",
                )
            )

        policy_query = _policy_query_from_text(user_query)
        if policy_query:
            search_query, topic = policy_query
            arguments = {"query": search_query}
            if topic:
                arguments["topic"] = topic
            calls.append(
                ToolCall(
                    name="search_policy_docs",
                    arguments=arguments,
                    reason="The query asks about a company rule or policy-like topic.",
                )
            )

        refund_arguments = _extract_refund_arguments(user_query)
        if refund_arguments:
            amount, percent = refund_arguments
            calls.append(
                ToolCall(
                    name="calculate_refund",
                    arguments={"amount": amount, "percent": percent},
                    reason="The query asks for a deterministic percentage calculation.",
                )
            )

        weather_city = _extract_weather_city(user_query)
        if weather_city:
            calls.append(
                ToolCall(
                    name="get_weather_snapshot",
                    arguments={"city": weather_city},
                    reason="The query asks for weather information for a city.",
                )
            )

        return calls

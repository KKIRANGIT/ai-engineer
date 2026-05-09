"""Validation layer for requested tool calls."""

from __future__ import annotations

import re
from typing import Any


class ValidationError(ValueError):
    """Raised when tool arguments fail validation."""


def _require_string(arguments: dict[str, Any], field_name: str) -> str:
    value = arguments.get(field_name)
    if not isinstance(value, str):
        raise ValidationError(f"{field_name} must be a string.")

    cleaned = value.strip()
    if not cleaned:
        raise ValidationError(f"{field_name} cannot be empty.")

    return cleaned


def _require_number(arguments: dict[str, Any], field_name: str) -> float:
    value = arguments.get(field_name)
    if not isinstance(value, (int, float)):
        raise ValidationError(f"{field_name} must be numeric.")

    return float(value)


def validate_tool_arguments(tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if tool_name == "lookup_ticket":
        ticket_id = _require_string(arguments, "ticket_id").upper()
        if not re.fullmatch(r"T-\d{4}", ticket_id):
            raise ValidationError("ticket_id must look like T-1002.")
        return {"ticket_id": ticket_id}

    if tool_name == "search_policy_docs":
        query = _require_string(arguments, "query")
        if len(query) < 3:
            raise ValidationError("query must be at least 3 characters long.")

        validated = {"query": query}
        topic = arguments.get("topic")
        if topic is not None:
            validated["topic"] = _require_string(arguments, "topic").lower()
        return validated

    if tool_name == "calculate_refund":
        amount = _require_number(arguments, "amount")
        percent = _require_number(arguments, "percent")
        if amount <= 0:
            raise ValidationError("amount must be greater than zero.")
        if percent < 0 or percent > 100:
            raise ValidationError("percent must be between 0 and 100.")
        return {"amount": amount, "percent": percent}

    if tool_name == "get_weather_snapshot":
        city = _require_string(arguments, "city").title()
        return {"city": city}

    raise ValidationError(f"Unknown tool: {tool_name}")

"""Deterministic tool implementations for the Week 13 lab."""

from __future__ import annotations

from typing import Any

from .data_access import WorkspaceDataStore


def lookup_ticket(store: WorkspaceDataStore, arguments: dict[str, Any]) -> dict[str, Any]:
    ticket_id = str(arguments["ticket_id"])
    ticket = store.get_ticket(ticket_id)

    if ticket is None:
        return {"found": False, "ticket_id": ticket_id, "message": "No matching ticket was found."}

    return {"found": True, "ticket": ticket}


def search_policy_docs(store: WorkspaceDataStore, arguments: dict[str, Any]) -> dict[str, Any]:
    query = str(arguments["query"])
    topic = arguments.get("topic")
    matches = store.search_policies(query=query, topic=str(topic) if topic else None)

    if not matches:
        return {"found": False, "query": query, "matches": []}

    return {"found": True, "query": query, "matches": matches}


def calculate_refund(store: WorkspaceDataStore, arguments: dict[str, Any]) -> dict[str, Any]:
    _ = store
    amount = float(arguments["amount"])
    percent = float(arguments["percent"])
    refund_value = round(amount * (percent / 100), 2)

    return {
        "amount": amount,
        "percent": percent,
        "refund_value": refund_value,
        "remaining_amount": round(amount - refund_value, 2),
    }


def get_weather_snapshot(store: WorkspaceDataStore, arguments: dict[str, Any]) -> dict[str, Any]:
    city = str(arguments["city"])
    snapshot = store.get_weather(city)

    if snapshot is None:
        return {"found": False, "city": city, "message": "City is not available in the local weather dataset."}

    return {"found": True, "snapshot": snapshot}


TOOL_FUNCTIONS = {
    "lookup_ticket": lookup_ticket,
    "search_policy_docs": search_policy_docs,
    "calculate_refund": calculate_refund,
    "get_weather_snapshot": get_weather_snapshot,
}


def execute_tool(store: WorkspaceDataStore, tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    if tool_name not in TOOL_FUNCTIONS:
        raise ValueError(f"Unknown tool: {tool_name}")

    return TOOL_FUNCTIONS[tool_name](store, arguments)

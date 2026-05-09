"""Shared tool definitions used for local execution and provider payload builders."""

from __future__ import annotations

from copy import deepcopy


TOOL_DEFINITIONS = [
    {
        "name": "lookup_ticket",
        "description": (
            "Look up a support ticket by ticket_id when the user needs the ticket summary, owner, status, or priority. "
            "Use this tool only for identifiers shaped like T-1002. Do not use it for policy questions, weather, or "
            "numeric calculations. The tool returns local mock ticket data from the Week 13 workspace."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {
                    "type": "string",
                    "description": "Ticket identifier such as T-1002.",
                }
            },
            "required": ["ticket_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "search_policy_docs",
        "description": (
            "Search internal policy summaries when the user asks about company rules such as refunds, leave, travel, "
            "equipment, or security. Use this when the answer should come from policy text instead of a guessed model "
            "answer. Do not use it for ticket lookup or math. The query should be a short search phrase, and topic can "
            "narrow the search when the domain is already clear."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "A short search phrase like 'refund policy' or 'travel reimbursement'.",
                },
                "topic": {
                    "type": "string",
                    "description": "Optional topic filter such as refund, leave, travel, equipment, or security.",
                },
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "calculate_refund",
        "description": (
            "Calculate a refund amount from a base amount and percentage. Use this tool when the user explicitly asks "
            "for a numeric refund calculation. Do not use it to decide whether a refund is allowed; that policy question "
            "belongs to the policy search tool. The percent value must be between 0 and 100."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "Base amount before the refund is applied.",
                },
                "percent": {
                    "type": "number",
                    "description": "Refund percentage between 0 and 100.",
                },
            },
            "required": ["amount", "percent"],
            "additionalProperties": False,
        },
    },
    {
        "name": "get_weather_snapshot",
        "description": (
            "Return a local mock weather snapshot for a supported city when the user asks about weather or temperature. "
            "Use this only for quick weather checks. Do not use it for policy lookup, tickets, or calculations. The city "
            "name should be written clearly, such as Bengaluru or London."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Supported city name such as Bengaluru, London, or New York.",
                }
            },
            "required": ["city"],
            "additionalProperties": False,
        },
    },
]


def get_tool_definitions() -> list[dict[str, object]]:
    return deepcopy(TOOL_DEFINITIONS)

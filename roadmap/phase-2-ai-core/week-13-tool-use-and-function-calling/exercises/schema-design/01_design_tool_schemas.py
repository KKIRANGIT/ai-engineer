"""Compare weak and strong tool schema design."""

from __future__ import annotations

import json


def main() -> None:
    weak_schema = {
        "name": "search_docs",
        "description": "Search documents.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
            },
        },
    }

    strong_schema = {
        "name": "search_policy_docs",
        "description": (
            "Search internal policy summaries when the user asks about company rules, "
            "refunds, leave, travel, equipment, or security. Use this tool when the "
            "answer should come from policy text instead of model memory. Do not use "
            "it for ticket lookup or numeric calculations."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "A short search phrase such as 'refund policy' or 'travel reimbursement'.",
                },
                "topic": {
                    "type": "string",
                    "description": "Optional topic filter such as refund, leave, travel, security, or equipment.",
                },
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    }

    print("Weak schema:\n")
    print(json.dumps(weak_schema, indent=2))
    print("\nStrong schema:\n")
    print(json.dumps(strong_schema, indent=2))


if __name__ == "__main__":
    main()

"""Local policy snippets used by the retrieval-aware system variant."""

from __future__ import annotations


KNOWLEDGE_BASE = {
    "refund": "manager approval",
    "travel": "receipts within 15 days",
    "security": "security review",
    "billing": "invoice history",
}


def lookup_policy_hint(category: str) -> str | None:
    return KNOWLEDGE_BASE.get(category)

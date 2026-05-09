"""Deterministic business helpers used by the capstone workflow."""

from __future__ import annotations


def decide_priority(category: str, ticket_text: str) -> str:
    text = ticket_text.lower()
    if category == "security":
        return "high"
    if "today" in text or "urgent" in text or "locked out" in text:
        return "high"
    if category in {"refund", "billing"}:
        return "medium"
    return "low"


def calculate_sla_hours(priority: str, customer_tier: str) -> int:
    base = {"high": 4, "medium": 12, "low": 24}[priority]
    if customer_tier == "enterprise":
        return max(2, base // 2)
    return base


def should_escalate(category: str, priority: str, customer_tier: str) -> bool:
    if category == "security":
        return True
    if priority == "high" and customer_tier == "enterprise":
        return True
    return False

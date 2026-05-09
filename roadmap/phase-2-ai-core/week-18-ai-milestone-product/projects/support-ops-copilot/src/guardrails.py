"""Safety checks for support ticket input."""

from __future__ import annotations

from .models import Ticket


SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "export customer database",
]


def screen_ticket(ticket: Ticket) -> tuple[bool, list[str]]:
    haystack = f"{ticket.title} {ticket.body}".lower()
    findings = [pattern for pattern in SUSPICIOUS_PATTERNS if pattern in haystack]
    return (len(findings) == 0, findings)

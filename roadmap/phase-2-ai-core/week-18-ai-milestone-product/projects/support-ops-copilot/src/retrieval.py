"""Simple policy retrieval for the Week 18 capstone."""

from __future__ import annotations

from .case_loader import load_policies
from .models import PolicyNote, Ticket


def _infer_topic(ticket: Ticket) -> str:
    text = f"{ticket.title} {ticket.body}".lower()
    if "refund" in text or "charge" in text:
        return "refund"
    if "invoice" in text or "billing" in text:
        return "billing"
    if "password" in text or "mfa" in text or "security" in text:
        return "security"
    return "general"


def retrieve_policy_notes(ticket: Ticket, limit: int = 2) -> list[PolicyNote]:
    topic = _infer_topic(ticket)
    matches = [note for note in load_policies() if note.topic == topic]
    return matches[:limit]


def infer_category(ticket: Ticket) -> str:
    return _infer_topic(ticket)

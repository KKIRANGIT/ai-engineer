"""Load tickets, policies, and eval cases for the Week 18 capstone."""

from __future__ import annotations

import json
from pathlib import Path

from .models import EvalCase, PolicyNote, Ticket


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"


def _load_json(filename: str) -> list[dict[str, object]]:
    path = DATA_DIR / filename
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_tickets() -> list[Ticket]:
    return [Ticket(**item) for item in _load_json("tickets.json")]


def get_ticket(ticket_id: str) -> Ticket:
    for ticket in load_tickets():
        if ticket.ticket_id == ticket_id:
            return ticket
    raise ValueError(f"Unknown ticket_id: {ticket_id}")


def load_policies() -> list[PolicyNote]:
    return [PolicyNote(**item) for item in _load_json("policies.json")]


def load_eval_cases() -> list[EvalCase]:
    return [EvalCase(**item) for item in _load_json("eval_cases.json")]

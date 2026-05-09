"""Shared models for the Week 18 capstone project."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class Ticket:
    ticket_id: str
    title: str
    body: str
    customer_tier: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class PolicyNote:
    note_id: str
    topic: str
    title: str
    summary: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AnalysisOutput:
    ticket_id: str
    category: str
    priority: str
    recommended_action: str
    source_titles: list[str]
    sla_hours: int
    escalation_needed: bool
    cost_estimate: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class EvalCase:
    ticket_id: str
    expected_category: str
    expected_priority: str
    expected_escalation: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

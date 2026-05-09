"""Shared data models for the Week 15 eval lab."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class EvalCase:
    case_id: str
    ticket_text: str
    expected_category: str
    expected_priority: str
    expected_next_action: str
    required_policy_phrase: str | None
    expected_tone: str
    likely_fix: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class SystemOutput:
    category: str
    priority: str
    next_action: str
    customer_reply: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CaseScore:
    case_id: str
    variant: str
    checks: dict[str, int]
    total_score: int
    max_score: int
    notes: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

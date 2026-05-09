"""Shared models for the Week 17 guarded assistant lab."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class RequestCase:
    case_id: str
    user_input: str
    retrieved_note: str
    expected_risk: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class RunResult:
    case_id: str
    risk_level: str
    blocked: bool
    estimated_cost: float
    response_text: str
    trace_path: str


@dataclass
class TraceEvent:
    stage: str
    payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

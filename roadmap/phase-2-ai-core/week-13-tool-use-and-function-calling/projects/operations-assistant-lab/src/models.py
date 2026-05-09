"""Data models shared across the Week 13 tool-calling project."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class ToolOutcome:
    name: str
    arguments: dict[str, Any]
    ok: bool
    output: dict[str, Any] | None = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class AssistantResult:
    user_query: str
    planned_calls: list[ToolCall]
    outcomes: list[ToolOutcome]
    final_answer: str
    trace_path: str

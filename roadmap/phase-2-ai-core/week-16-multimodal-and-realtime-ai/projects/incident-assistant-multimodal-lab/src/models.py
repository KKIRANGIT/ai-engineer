"""Shared data models for the Week 16 project."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class IncidentCase:
    case_id: str
    title: str
    text_report: str
    transcript_excerpt: str
    image_observations: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class IncidentResult:
    case_id: str
    mode: str
    summary: str
    streamed_chunks: list[str]
    trace_path: str


@dataclass
class SessionEvent:
    stage: str
    payload: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

"""Shared state models for the Week 14 orchestration project."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class StepRecord:
    stage: str
    details: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class WorkflowState:
    query: str
    topics: list[str] = field(default_factory=list)
    retrieval_query: str = ""
    retrieved_docs: list[dict[str, Any]] = field(default_factory=list)
    retry_count: int = 0
    needs_human_review: bool = False
    brief: str = ""
    step_history: list[StepRecord] = field(default_factory=list)

    def add_step(self, stage: str, details: dict[str, Any]) -> None:
        self.step_history.append(StepRecord(stage=stage, details=details))

    def to_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "topics": self.topics,
            "retrieval_query": self.retrieval_query,
            "retrieved_docs": self.retrieved_docs,
            "retry_count": self.retry_count,
            "needs_human_review": self.needs_human_review,
            "brief": self.brief,
            "step_history": [step.to_dict() for step in self.step_history],
        }


@dataclass
class RunResult:
    mode: str
    final_brief: str
    needs_human_review: bool
    trace_path: str
    state: WorkflowState

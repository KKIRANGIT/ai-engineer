from dataclasses import dataclass


@dataclass
class Ticket:
    ticket_id: str
    text: str
    expected_category: str


@dataclass
class TriageResult:
    category: str
    priority: str
    summary: str
    needs_human_follow_up: bool
    confidence_note: str


@dataclass
class RegressionCase:
    ticket_id: str
    expected: dict


@dataclass
class RegressionOutcome:
    ticket_id: str
    passed: bool
    failures: list[str]
    result: dict

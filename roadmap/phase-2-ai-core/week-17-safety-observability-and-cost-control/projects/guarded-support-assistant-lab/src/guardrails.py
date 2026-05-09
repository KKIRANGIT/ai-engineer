"""Lightweight guardrails for suspicious or unsafe input patterns."""

from __future__ import annotations

from .models import RequestCase


SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden instructions",
    "send raw customer records",
]


def assess_risk(case: RequestCase) -> tuple[str, list[str]]:
    findings: list[str] = []
    haystack = f"{case.user_input} {case.retrieved_note}".lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in haystack:
            findings.append(pattern)

    if findings:
        return "high", findings

    if len(case.user_input) > 400:
        return "medium", ["large input size"]

    return "low", []


def should_block(risk_level: str) -> bool:
    return risk_level == "high"

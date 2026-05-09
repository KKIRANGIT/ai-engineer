"""Simple trust-boundary classification helpers."""

from __future__ import annotations

from .models import RequestCase


def classify_trust_boundaries(case: RequestCase) -> dict[str, str]:
    return {
        "system_policy": "trusted",
        "user_input": "untrusted",
        "retrieved_note": "untrusted",
        "tool_output": "conditionally_trusted",
    }

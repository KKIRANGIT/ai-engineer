"""Evaluation helpers for the Week 18 capstone."""

from __future__ import annotations

from .analyzer import analyze_ticket
from .case_loader import load_eval_cases


def run_eval() -> dict[str, object]:
    case_results: list[dict[str, object]] = []
    passed = 0

    for case in load_eval_cases():
        output = analyze_ticket(case.ticket_id)
        category_ok = output.category == case.expected_category
        priority_ok = output.priority == case.expected_priority
        escalation_ok = output.escalation_needed == case.expected_escalation

        if category_ok and priority_ok and escalation_ok:
            passed += 1

        case_results.append(
            {
                "ticket_id": case.ticket_id,
                "category_ok": category_ok,
                "priority_ok": priority_ok,
                "escalation_ok": escalation_ok,
            }
        )

    return {
        "case_count": len(case_results),
        "passed": passed,
        "average_score": round(passed / len(case_results), 3) if case_results else 0.0,
        "case_results": case_results,
    }

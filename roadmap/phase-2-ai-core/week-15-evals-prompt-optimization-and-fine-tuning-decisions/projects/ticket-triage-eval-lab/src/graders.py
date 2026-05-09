"""Programmatic graders for the Week 15 eval lab."""

from __future__ import annotations

from .models import CaseScore, EvalCase, SystemOutput


def grade_case(case: EvalCase, variant: str, output: SystemOutput) -> CaseScore:
    checks: dict[str, int] = {}
    notes: list[str] = []

    checks["schema_complete"] = int(
        all([output.category, output.priority, output.next_action, output.customer_reply])
    )
    if not checks["schema_complete"]:
        notes.append("Missing required output fields.")

    checks["category_match"] = int(output.category == case.expected_category)
    if not checks["category_match"]:
        notes.append(f"Expected category {case.expected_category}, got {output.category}.")

    checks["priority_match"] = int(output.priority == case.expected_priority)
    if not checks["priority_match"]:
        notes.append(f"Expected priority {case.expected_priority}, got {output.priority}.")

    checks["next_action_match"] = int(case.expected_next_action.lower() in output.next_action.lower())
    if not checks["next_action_match"]:
        notes.append("Next action did not align with the expected workflow.")

    checks["tone_quality"] = int("thanks" in output.customer_reply.lower() or "thank you" in output.customer_reply.lower())
    if not checks["tone_quality"]:
        notes.append("Reply tone lacked a clear acknowledgement.")

    if case.required_policy_phrase:
        checks["policy_guidance"] = int(case.required_policy_phrase.lower() in output.customer_reply.lower())
        if not checks["policy_guidance"]:
            notes.append(f"Missing policy phrase: {case.required_policy_phrase}.")
    else:
        checks["policy_guidance"] = 1

    total_score = sum(checks.values())
    return CaseScore(
        case_id=case.case_id,
        variant=variant,
        checks=checks,
        total_score=total_score,
        max_score=len(checks),
        notes=notes,
    )

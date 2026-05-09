"""Run evaluation variants and summarize results."""

from __future__ import annotations

from .dataset import load_eval_cases
from .graders import grade_case
from .models import CaseScore
from .systems import run_system


def run_variant(variant: str) -> list[CaseScore]:
    scores: list[CaseScore] = []
    for case in load_eval_cases():
        output = run_system(case, variant)
        scores.append(grade_case(case, variant, output))
    return scores


def summarize_scores(scores: list[CaseScore]) -> dict[str, object]:
    total_points = sum(score.total_score for score in scores)
    max_points = sum(score.max_score for score in scores)
    average = round(total_points / max_points, 3) if max_points else 0.0

    failing_cases = [score.case_id for score in scores if score.total_score < score.max_score]
    metric_totals: dict[str, int] = {}

    for score in scores:
        for metric, value in score.checks.items():
            metric_totals[metric] = metric_totals.get(metric, 0) + value

    return {
        "case_count": len(scores),
        "total_points": total_points,
        "max_points": max_points,
        "average_score": average,
        "failing_cases": failing_cases,
        "metric_totals": metric_totals,
    }


def compare_variants(variants: list[str]) -> dict[str, dict[str, object]]:
    return {variant: summarize_scores(run_variant(variant)) for variant in variants}

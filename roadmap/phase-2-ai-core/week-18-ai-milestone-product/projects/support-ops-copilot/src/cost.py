"""Rough request cost estimation for the capstone workflow."""

from __future__ import annotations


INPUT_COST_PER_1K = 0.002
OUTPUT_COST_PER_1K = 0.006


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def estimate_cost(input_text: str, output_text: str) -> float:
    input_tokens = estimate_tokens(input_text)
    output_tokens = estimate_tokens(output_text)
    cost = (input_tokens / 1000) * INPUT_COST_PER_1K + (output_tokens / 1000) * OUTPUT_COST_PER_1K
    return round(cost, 6)

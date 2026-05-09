"""Simple request cost estimation and budget checks."""

from __future__ import annotations


INPUT_COST_PER_1K = 0.002
OUTPUT_COST_PER_1K = 0.006
BUDGET_LIMIT = 0.01


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def estimate_request_cost(user_input: str, retrieved_note: str, response_text: str) -> float:
    input_tokens = estimate_tokens(user_input) + estimate_tokens(retrieved_note)
    output_tokens = estimate_tokens(response_text)
    cost = (input_tokens / 1000) * INPUT_COST_PER_1K + (output_tokens / 1000) * OUTPUT_COST_PER_1K
    return round(cost, 6)


def over_budget(cost: float) -> bool:
    return cost > BUDGET_LIMIT

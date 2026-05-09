"""Generate a simple decision memo from evaluation results."""

from __future__ import annotations

from .analysis import compare_variants


def generate_decision_memo() -> str:
    results = compare_variants(["baseline", "prompt_v2", "retrieval_v1"])
    baseline = results["baseline"]
    prompt_v2 = results["prompt_v2"]
    retrieval_v1 = results["retrieval_v1"]

    lines = ["Optimization decision memo", ""]
    lines.append(f"Baseline average score: {baseline['average_score']}")
    lines.append(f"Prompt_v2 average score: {prompt_v2['average_score']}")
    lines.append(f"Retrieval_v1 average score: {retrieval_v1['average_score']}")
    lines.append("")

    if prompt_v2["average_score"] > baseline["average_score"]:
        lines.append("Prompt_v2 improved general instruction-following and tone.")

    if retrieval_v1["average_score"] > prompt_v2["average_score"]:
        lines.append("Retrieval_v1 further improved policy-aware answers, suggesting knowledge access was a real bottleneck.")

    lines.append("")
    lines.append("Recommended interpretation:")

    if retrieval_v1["average_score"] > prompt_v2["average_score"] > baseline["average_score"]:
        lines.append("- Fix prompt clarity first, then add retrieval or context when factual guidance is missing.")
        lines.append("- Fine-tuning is not the first recommendation because the measured gains still come from system design changes.")
    elif prompt_v2["average_score"] > baseline["average_score"]:
        lines.append("- Prompt optimization appears to be the highest-leverage next step.")
    else:
        lines.append("- If prompt changes do not materially help, inspect retrieval, tooling, or dataset labels before considering fine-tuning.")

    lines.append("")
    lines.append("Fine-tuning should be considered only if the remaining failures are consistent, repeated, and still present after prompt and retrieval improvements.")
    return "\n".join(lines)

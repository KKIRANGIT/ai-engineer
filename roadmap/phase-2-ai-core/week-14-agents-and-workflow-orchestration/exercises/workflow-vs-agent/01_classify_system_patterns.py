"""Classify whether a system is closer to a workflow or an agent loop."""

from __future__ import annotations


def classify(description: str) -> str:
    text = description.lower()

    if "fixed order" in text or "explicit step" in text:
        return "workflow-like"
    if "choose next tool" in text or "dynamic path" in text:
        return "agent-like"
    return "mixed"


def main() -> None:
    examples = [
        "A pipeline with fixed order steps: classify, retrieve, draft, review.",
        "A system that can choose next tool calls based on new observations.",
        "A graph with explicit routing plus one dynamic retry decision.",
    ]

    for example in examples:
        print(f"{classify(example)} -> {example}")


if __name__ == "__main__":
    main()

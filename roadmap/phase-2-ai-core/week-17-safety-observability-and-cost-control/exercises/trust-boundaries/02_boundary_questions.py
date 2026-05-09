"""List useful trust-boundary questions for an AI workflow."""

from __future__ import annotations


def main() -> None:
    questions = [
        "What input is trusted?",
        "What input is untrusted?",
        "What content can influence tool behavior?",
        "What should never be executed without validation?",
    ]

    for question in questions:
        print(f"- {question}")


if __name__ == "__main__":
    main()

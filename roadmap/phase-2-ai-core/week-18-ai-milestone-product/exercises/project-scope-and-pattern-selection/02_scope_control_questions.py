"""List the scoping questions that keep milestone projects credible."""

from __future__ import annotations


def main() -> None:
    questions = [
        "What user problem is being solved?",
        "Which AI pattern is actually needed?",
        "What will not be built this week?",
        "How will quality be shown visibly?",
    ]

    for question in questions:
        print(f"- {question}")


if __name__ == "__main__":
    main()

"""Explain when plain code is enough for orchestration."""

from __future__ import annotations


def main() -> None:
    cases = [
        "A four-step pipeline with known order and no pause/resume requirement.",
        "A branching workflow with retries and human approval checkpoints.",
    ]

    for case in cases:
        if "known order" in case:
            print(f"Plain code is enough: {case}")
        else:
            print(f"A graph runtime may help: {case}")


if __name__ == "__main__":
    main()

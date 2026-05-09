"""Show how vague quality goals become measurable checks."""

from __future__ import annotations


def main() -> None:
    vague_goal = "The answer should be good."
    measurable_checks = [
        "category must match expected label",
        "priority must match expected severity",
        "reply must acknowledge the user",
        "policy phrase must appear when domain guidance is needed",
    ]

    print("Vague goal:")
    print(vague_goal)
    print("\nMeasurable checks:")
    for check in measurable_checks:
        print(f"- {check}")


if __name__ == "__main__":
    main()

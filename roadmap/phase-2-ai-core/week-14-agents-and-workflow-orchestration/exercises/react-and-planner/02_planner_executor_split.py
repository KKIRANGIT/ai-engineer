"""Separate planning from execution in a tiny example."""

from __future__ import annotations


def make_plan(query: str) -> list[str]:
    plan: list[str] = []
    if "refund" in query.lower():
        plan.append("search refund docs")
    if "security" in query.lower():
        plan.append("search security docs")
    plan.append("write summary")
    return plan


def execute_plan(plan: list[str]) -> None:
    for step in plan:
        print(f"Executing: {step}")


def main() -> None:
    query = "Summarize refund policy and security requirements."
    plan = make_plan(query)
    print("Plan:", plan)
    execute_plan(plan)


if __name__ == "__main__":
    main()

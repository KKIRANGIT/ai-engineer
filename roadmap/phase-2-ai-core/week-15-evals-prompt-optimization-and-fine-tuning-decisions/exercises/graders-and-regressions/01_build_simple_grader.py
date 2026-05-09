"""Build a tiny programmatic grader."""

from __future__ import annotations


def grade(expected: str, actual: str) -> int:
    return int(expected == actual)


def main() -> None:
    print(grade("refund", "refund"))
    print(grade("refund", "billing"))


if __name__ == "__main__":
    main()

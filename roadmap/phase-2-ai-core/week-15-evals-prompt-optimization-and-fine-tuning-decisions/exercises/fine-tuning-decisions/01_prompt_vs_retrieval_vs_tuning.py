"""Map failure patterns to likely optimization levers."""

from __future__ import annotations


def recommend(failure_pattern: str) -> str:
    mapping = {
        "formatting inconsistency": "prompt or structured output",
        "missing policy facts": "retrieval or context improvement",
        "stable repeated behavior gap": "consider fine-tuning after eval validation",
    }
    return mapping.get(failure_pattern, "diagnose the failure more clearly first")


def main() -> None:
    patterns = [
        "formatting inconsistency",
        "missing policy facts",
        "stable repeated behavior gap",
    ]

    for pattern in patterns:
        print(f"{pattern} -> {recommend(pattern)}")


if __name__ == "__main__":
    main()

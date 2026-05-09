"""Show why a representative dataset needs more than easy examples."""

from __future__ import annotations


def main() -> None:
    cases = {
        "easy": "refund request with clear wording",
        "ambiguous": "billing issue that may be refund-related",
        "edge": "security issue phrased as an account problem",
        "failure_history": "travel receipt submitted after delay",
    }

    for label, example in cases.items():
        print(f"{label}: {example}")


if __name__ == "__main__":
    main()

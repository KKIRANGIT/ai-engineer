"""Demonstrate structural validation before tool execution."""

from __future__ import annotations


def validate_refund_arguments(arguments: dict[str, object]) -> list[str]:
    errors: list[str] = []

    amount = arguments.get("amount")
    percent = arguments.get("percent")

    if not isinstance(amount, (int, float)):
        errors.append("amount must be numeric")
    elif amount <= 0:
        errors.append("amount must be greater than zero")

    if not isinstance(percent, (int, float)):
        errors.append("percent must be numeric")
    elif percent < 0 or percent > 100:
        errors.append("percent must stay between 0 and 100")

    return errors


def main() -> None:
    samples = [
        {"amount": 1200, "percent": 50},
        {"amount": 1200, "percent": 150},
        {"amount": "twelve hundred", "percent": 50},
    ]

    for sample in samples:
        errors = validate_refund_arguments(sample)
        print(f"Input: {sample}")
        print("Valid" if not errors else f"Errors: {errors}")
        print()


if __name__ == "__main__":
    main()

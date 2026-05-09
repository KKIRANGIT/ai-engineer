"""List the fields a useful AI request trace should include."""

from __future__ import annotations


def main() -> None:
    fields = [
        "request id",
        "risk level",
        "latency",
        "estimated tokens",
        "estimated cost",
        "guardrail outcome",
        "retry count",
        "response status",
    ]

    for field in fields:
        print(f"- {field}")


if __name__ == "__main__":
    main()

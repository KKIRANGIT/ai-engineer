"""Show why applications must decide whether a tool call should execute."""

from __future__ import annotations


def should_execute(tool_name: str, arguments: dict[str, object]) -> tuple[bool, str]:
    if tool_name == "delete_customer_account":
        return False, "High-risk actions should not run in this beginner lab."

    if tool_name == "calculate_refund":
        percent = arguments.get("percent")
        if not isinstance(percent, (int, float)):
            return False, "Refund percentage must be numeric."
        if percent < 0 or percent > 100:
            return False, "Refund percentage must stay between 0 and 100."

    return True, "The tool call passed the pre-checks."


def main() -> None:
    samples = [
        ("calculate_refund", {"amount": 1200, "percent": 50}),
        ("calculate_refund", {"amount": 1200, "percent": 250}),
        ("delete_customer_account", {"customer_id": "C-77"}),
    ]

    for tool_name, arguments in samples:
        allowed, reason = should_execute(tool_name, arguments)
        print(f"{tool_name}: allowed={allowed}")
        print(f"Reason: {reason}\n")


if __name__ == "__main__":
    main()

"""Show business-rule checks beyond simple schema validation."""

from __future__ import annotations


def can_process_refund(amount: float, percent: float, role: str) -> tuple[bool, str]:
    if role not in {"agent", "manager"}:
        return False, "Unknown role."

    refund_value = amount * (percent / 100)

    if role == "agent" and refund_value > 500:
        return False, "Agents can review the request but cannot approve refunds above 500."

    return True, "The request is inside the current approval boundary."


def main() -> None:
    samples = [
        (1200, 25, "agent"),
        (1200, 60, "agent"),
        (1200, 60, "manager"),
    ]

    for amount, percent, role in samples:
        allowed, reason = can_process_refund(amount, percent, role)
        print(f"role={role}, amount={amount}, percent={percent}")
        print(f"allowed={allowed}")
        print(f"reason={reason}\n")


if __name__ == "__main__":
    main()

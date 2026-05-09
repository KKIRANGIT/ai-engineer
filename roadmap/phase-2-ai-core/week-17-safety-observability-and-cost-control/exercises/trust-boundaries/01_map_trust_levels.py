"""Show that different inputs deserve different trust levels."""

from __future__ import annotations


def main() -> None:
    trust_map = {
        "system_policy": "trusted",
        "user_input": "untrusted",
        "retrieved_note": "untrusted",
        "tool_output": "conditionally_trusted",
    }

    for source, trust_level in trust_map.items():
        print(f"{source}: {trust_level}")


if __name__ == "__main__":
    main()

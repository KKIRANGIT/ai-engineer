"""Different vision tasks need different application designs."""

from __future__ import annotations


def main() -> None:
    tasks = [
        "receipt field extraction",
        "screenshot question answering",
        "general scene understanding",
    ]
    for task in tasks:
        print(f"- {task}")


if __name__ == "__main__":
    main()

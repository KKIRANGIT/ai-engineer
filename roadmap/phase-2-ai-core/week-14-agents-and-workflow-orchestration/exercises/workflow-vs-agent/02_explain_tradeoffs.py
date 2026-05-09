"""Explain why more flexibility is not automatically better."""

from __future__ import annotations


def compare(complexity: int, flexibility: int) -> str:
    if flexibility <= complexity:
        return "Use the simpler workflow unless the task truly needs dynamic branching."
    return "Extra flexibility may be justified, but inspectability still matters."


def main() -> None:
    samples = [(8, 3), (5, 7), (6, 6)]

    for complexity, flexibility in samples:
        print(f"complexity={complexity}, flexibility={flexibility}")
        print(compare(complexity, flexibility))
        print()


if __name__ == "__main__":
    main()

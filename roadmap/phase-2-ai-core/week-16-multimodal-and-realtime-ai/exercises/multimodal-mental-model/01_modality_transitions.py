"""Show why multimodal systems should be thought of as transition pipelines."""

from __future__ import annotations


def main() -> None:
    transitions = [
        "audio -> transcript -> reasoning",
        "image -> structured observations -> reasoning",
        "text -> streamed response chunks",
    ]

    for transition in transitions:
        print(f"- {transition}")


if __name__ == "__main__":
    main()

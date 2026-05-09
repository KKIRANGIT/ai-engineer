"""Contrast chained voice pipelines with low-latency realtime paths."""

from __future__ import annotations


def main() -> None:
    print("Chained pipeline: speech-to-text -> text model -> text-to-speech")
    print("Realtime path: ongoing session with low-latency multimodal turn handling")


if __name__ == "__main__":
    main()

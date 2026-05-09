"""Show the shape of a realtime-style session event flow."""

from __future__ import annotations


def main() -> None:
    events = [
        "session_started",
        "input_received",
        "transcript_ready",
        "vision_ready",
        "response_chunk",
        "session_completed",
    ]
    for event in events:
        print(event)


if __name__ == "__main__":
    main()

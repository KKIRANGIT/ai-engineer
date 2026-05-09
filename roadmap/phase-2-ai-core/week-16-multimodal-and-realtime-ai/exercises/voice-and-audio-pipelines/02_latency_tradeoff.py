"""Show how more control can increase latency."""

from __future__ import annotations


def main() -> None:
    print("Chained pipelines are often easier to inspect, but every stage can add delay.")
    print("Realtime paths can feel more natural, but session control becomes more complex.")


if __name__ == "__main__":
    main()

"""Show how weak evidence can trigger a human review checkpoint."""

from __future__ import annotations


def needs_review(topic_count: int, covered_topic_count: int) -> bool:
    return covered_topic_count < topic_count


def main() -> None:
    scenarios = [(2, 2), (2, 1), (1, 0)]

    for topic_count, covered_topic_count in scenarios:
        review = needs_review(topic_count, covered_topic_count)
        print(f"topics={topic_count}, covered={covered_topic_count}, needs_review={review}")


if __name__ == "__main__":
    main()

"""Show the shape of a plan-act-observe loop."""

from __future__ import annotations


def main() -> None:
    observations: list[str] = []
    planned_topics = ["refund", "security"]

    for topic in planned_topics:
        print(f"Plan: search documents for {topic}")
        observation = f"Found evidence for {topic}"
        observations.append(observation)
        print(f"Observe: {observation}")
        print()

    print("Next step: synthesize a brief from observations.")
    print(observations)


if __name__ == "__main__":
    main()

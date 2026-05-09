"""
This exercise uses small hand-written vectors to show how semantically related
items cluster together more than unrelated items.
"""

from math import sqrt


def cosine_similarity(left: list[float], right: list[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    left_norm = sqrt(sum(value * value for value in left))
    right_norm = sqrt(sum(value * value for value in right))
    return dot / (left_norm * right_norm)


def main():
    vectors = {
        "refund request": [0.95, 0.05, 0.0],
        "billing problem": [0.9, 0.1, 0.0],
        "password reset": [0.05, 0.95, 0.0],
        "dashboard theme": [0.0, 0.05, 0.95],
    }

    comparisons = [
        ("refund request", "billing problem"),
        ("refund request", "password reset"),
        ("refund request", "dashboard theme"),
    ]

    for left_name, right_name in comparisons:
        score = cosine_similarity(vectors[left_name], vectors[right_name])
        print(f"{left_name!r} vs {right_name!r}: {score:.4f}")


if __name__ == "__main__":
    main()

"""
This exercise compares how keyword, semantic, and hybrid retrieval reward
different signals.
"""


def main():
    comparison = [
        {
            "document": "Refund Policy Overview",
            "keyword_score": 0.45,
            "semantic_score": 0.92,
            "hybrid_score": 0.685,
        },
        {
            "document": "Double Charge Troubleshooting",
            "keyword_score": 0.88,
            "semantic_score": 0.81,
            "hybrid_score": 0.845,
        },
    ]

    for row in comparison:
        print(row)


if __name__ == "__main__":
    main()

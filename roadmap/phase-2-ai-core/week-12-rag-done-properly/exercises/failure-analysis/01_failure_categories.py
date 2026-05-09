"""
This exercise turns RAG failures into named categories you can actually debug.
"""


def main():
    categories = [
        "Wrong document retrieved",
        "Right document but wrong chunk",
        "Right chunk but incomplete context packing",
        "Good context but poor answer synthesis",
        "Missing metadata filter or scope control",
        "Query wording did not reflect the retrieval need",
    ]

    for category in categories:
        print(f"- {category}")


if __name__ == "__main__":
    main()

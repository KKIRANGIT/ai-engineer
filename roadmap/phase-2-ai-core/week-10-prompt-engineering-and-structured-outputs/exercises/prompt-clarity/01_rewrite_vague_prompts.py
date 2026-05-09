"""
This exercise demonstrates how vague prompts can be tightened into
specification-like instructions.
"""


def build_examples():
    return [
        {
            "weak": "Summarize this ticket.",
            "strong": (
                "Read the support ticket. Return a short summary focused on the user's main problem, "
                "the product area involved, and any urgency signals."
            ),
        },
        {
            "weak": "Categorize this issue.",
            "strong": (
                "Classify the support ticket into one category from this list: billing, bug, account_access, "
                "feature_request, or unclear. If the ticket does not support a confident choice, use unclear."
            ),
        },
    ]


def main():
    for index, example in enumerate(build_examples(), start=1):
        print(f"\nExample {index}")
        print("Weak prompt:")
        print(example["weak"])
        print("Improved prompt:")
        print(example["strong"])


if __name__ == "__main__":
    main()

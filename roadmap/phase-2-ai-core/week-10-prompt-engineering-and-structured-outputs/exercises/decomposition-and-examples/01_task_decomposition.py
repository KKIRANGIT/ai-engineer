"""
This exercise shows how one messy task can be decomposed into cleaner prompt
steps before asking the model for a final output.
"""


def main():
    decomposition = [
        "Step 1: Identify the main user complaint.",
        "Step 2: Classify the issue category.",
        "Step 3: Estimate urgency from the text only.",
        "Step 4: Extract any promised follow-up action.",
        "Step 5: Return the final response as structured JSON.",
    ]

    print("A decomposed support-ticket prompt flow:")
    for step in decomposition:
        print(f"- {step}")


if __name__ == "__main__":
    main()

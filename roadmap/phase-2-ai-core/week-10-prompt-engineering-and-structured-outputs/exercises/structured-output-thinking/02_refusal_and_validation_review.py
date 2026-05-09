"""
This exercise reminds you that structured outputs still need application-side
validation and refusal-aware handling.
"""


def main():
    checklist = [
        "Did the model return a refusal instead of structured data?",
        "Are all required fields present?",
        "Do enum fields contain only supported values?",
        "Did the output omit information because the ticket was unclear?",
        "Should the app show a user-facing fallback instead of trusting the result?",
    ]

    print("Structured output review checklist:")
    for item in checklist:
        print(f"- {item}")


if __name__ == "__main__":
    main()

"""
This exercise shows how a user question can be rewritten into a search query
that is more likely to retrieve the correct evidence.
"""


def main():
    examples = [
        {
            "user_question": "What should happen if someone gets billed twice?",
            "retrieval_query": "duplicate charge refund billing dispute customer refund policy",
        },
        {
            "user_question": "I forgot my password and still can't log in. What now?",
            "retrieval_query": "password reset account locked sign in troubleshooting account access",
        },
    ]

    for example in examples:
        print("\nUser question:")
        print(example["user_question"])
        print("Retrieval-oriented rewrite:")
        print(example["retrieval_query"])


if __name__ == "__main__":
    main()

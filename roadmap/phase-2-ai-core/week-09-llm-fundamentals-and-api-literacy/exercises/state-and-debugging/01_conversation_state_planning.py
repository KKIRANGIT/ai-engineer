"""
This exercise compares stateless and stateful conversation strategies so you
can think about why some history should be retained and some should be summarized.
"""


def build_state_examples():
    return {
        "stateless_messages_model": {
            "approach": "Resend the message history you want the model to use.",
            "good_for": ["explicit control", "easy replay", "simple auditability"],
            "risk": "context can become large and expensive over time",
        },
        "response_chaining_model": {
            "approach": "Reference prior responses or conversations through provider-supported state.",
            "good_for": ["simpler client logic", "stateful workflows"],
            "risk": "you still need application-level decisions about what should persist",
        },
    }


def main():
    examples = build_state_examples()
    for name, details in examples.items():
        print(f"\n{name}:")
        for key, value in details.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    main()

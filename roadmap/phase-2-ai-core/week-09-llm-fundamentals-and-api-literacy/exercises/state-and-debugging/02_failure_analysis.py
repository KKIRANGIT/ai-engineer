"""
This file turns API failure analysis into a concrete checklist instead of a
guessing game.
"""


def build_failure_review():
    return [
        "Did the request use the intended model?",
        "Was the instruction layer present and clear?",
        "Was the payload structure valid for the provider?",
        "Was the output empty because of a stop condition or refusal?",
        "Did token usage or context size contribute to the failure?",
        "Was the error transport-level, authentication-level, or model-level?",
    ]


def main():
    print("Failure review checklist:")
    for item in build_failure_review():
        print(f"- {item}")


if __name__ == "__main__":
    main()

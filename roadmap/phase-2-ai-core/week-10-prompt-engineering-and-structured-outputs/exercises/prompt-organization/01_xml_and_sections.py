"""
This exercise demonstrates how XML-like tags can separate instructions,
examples, and source content in a long prompt.
"""


def build_tagged_prompt():
    return """
<instructions>
Classify the support ticket and return a response that matches the required schema.
Use only the categories provided.
</instructions>

<categories>
billing
bug
account_access
feature_request
unclear
</categories>

<example>
Input: "I was charged twice for my subscription renewal."
Output intent: billing, urgent enough for medium priority.
</example>

<ticket>
I cannot sign in after resetting my password. The reset email worked but the new password fails.
</ticket>
""".strip()


def main():
    print(build_tagged_prompt())


if __name__ == "__main__":
    main()

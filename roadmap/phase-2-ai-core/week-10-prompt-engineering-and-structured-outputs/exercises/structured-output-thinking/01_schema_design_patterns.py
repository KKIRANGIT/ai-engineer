"""
This exercise makes application-oriented schema design visible.
"""

import json


def build_schema():
    return {
        "type": "object",
        "properties": {
            "category": {
                "type": "string",
                "enum": ["billing", "bug", "account_access", "feature_request", "unclear"],
            },
            "priority": {
                "type": "string",
                "enum": ["low", "medium", "high"],
            },
            "summary": {"type": "string"},
            "needs_human_follow_up": {"type": "boolean"},
        },
        "required": ["category", "priority", "summary", "needs_human_follow_up"],
        "additionalProperties": False,
    }


def main():
    print(json.dumps(build_schema(), indent=2))


if __name__ == "__main__":
    main()

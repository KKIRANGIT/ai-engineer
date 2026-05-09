"""
Week 03 - JSON and Responses: Extract Only What You Need

What this file teaches:
- how JSON text becomes Python data
- how to inspect response shape
- how to extract selected fields instead of printing the entire payload
"""

import json

SAMPLE_USER_RESPONSE = """
{
  "login": "octocat",
  "id": 1,
  "name": "The Octocat",
  "public_repos": 8,
  "followers": 100,
  "following": 0,
  "html_url": "https://github.com/octocat"
}
"""


def parse_user_response(json_text):
    """Load JSON text and return only the fields we care about."""
    user_data = json.loads(json_text)

    return {
        "login": user_data["login"],
        "name": user_data["name"],
        "public_repos": user_data["public_repos"],
        "profile_url": user_data["html_url"],
    }


def show_example():
    """Demonstrate targeted parsing from a JSON response."""
    selected_fields = parse_user_response(SAMPLE_USER_RESPONSE)
    print("Selected fields:", selected_fields)


if __name__ == "__main__":
    show_example()

"""
Week 03 - Wrappers: Hiding Low-Level Details Behind Clean Functions

What this file teaches:
- how wrapper code can hide transport details
- how the rest of an application can ask for useful Python data instead of raw responses
"""


def fake_http_get_user(username):
    """Simulate a low-level HTTP call that returns raw response data."""
    return {
        "status_code": 200,
        "json_body": {
            "login": username,
            "name": "Demo User",
            "followers": 42,
        },
    }


def get_user_summary(username):
    """Return only the business-level fields the rest of the app needs."""
    response = fake_http_get_user(username)

    if response["status_code"] != 200:
        raise ValueError("User lookup failed.")

    user_data = response["json_body"]
    return {
        "username": user_data["login"],
        "display_name": user_data["name"],
        "followers": user_data["followers"],
    }


def show_example():
    """Demonstrate the difference between raw response data and wrapped output."""
    summary = get_user_summary("asha-dev")
    print("User summary:", summary)


if __name__ == "__main__":
    show_example()

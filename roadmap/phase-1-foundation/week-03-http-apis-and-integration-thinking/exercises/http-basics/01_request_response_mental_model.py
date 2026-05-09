"""
Week 03 - HTTP Basics: Request and Response Thinking

What this file teaches:
- what a request contains
- what a response contains
- how status code families help with debugging
"""


def build_example_request():
    """Return a small dictionary that models an HTTP request."""
    return {
        "method": "GET",
        "url": "https://api.example.com/users",
        "headers": {
            "Accept": "application/json",
            "User-Agent": "week-03-demo",
        },
        "body": None,
    }


def build_example_response():
    """Return a small dictionary that models an HTTP response."""
    return {
        "status_code": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": [{"id": 1, "name": "Asha"}],
    }


def describe_status_family(status_code):
    """Return the broad meaning of a status code family."""
    first_digit = status_code // 100

    if first_digit == 2:
        return "Success"
    if first_digit == 3:
        return "Redirection"
    if first_digit == 4:
        return "Client error"
    if first_digit == 5:
        return "Server error"

    return "Other"


def show_example():
    """Print the example request and response in a readable way."""
    request_data = build_example_request()
    response_data = build_example_response()

    print("Request method:", request_data["method"])
    print("Request URL:", request_data["url"])
    print("Request headers:", request_data["headers"])
    print("-" * 40)
    print("Response status:", response_data["status_code"])
    print("Status family:", describe_status_family(response_data["status_code"]))
    print("Response headers:", response_data["headers"])
    print("Response body:", response_data["body"])


if __name__ == "__main__":
    show_example()

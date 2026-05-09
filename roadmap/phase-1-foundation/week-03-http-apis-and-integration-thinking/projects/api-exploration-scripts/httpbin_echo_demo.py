"""
Use httpbin to inspect how query parameters and headers are reflected back.
"""

import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def fetch_echo_response():
    """Send a GET request with query parameters and a custom header."""
    query_string = urlencode({"topic": "http", "week": 3})
    url = f"https://httpbin.org/get?{query_string}"

    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "X-Demo-Client": "ai-engineer-week-03",
        },
    )

    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Print the echoed query arguments and a selected header."""
    try:
        response_data = fetch_echo_response()
        print("Echoed query args:", response_data["args"])
        print("Echoed URL:", response_data["url"])
    except Exception as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()

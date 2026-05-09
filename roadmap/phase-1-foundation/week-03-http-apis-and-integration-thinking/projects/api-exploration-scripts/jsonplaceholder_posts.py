"""
Explore simple GET and POST calls against JSONPlaceholder.
"""

import json
from urllib.request import Request, urlopen


def fetch_post(post_id):
    """Fetch one placeholder post by ID."""
    request = Request(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        headers={"Accept": "application/json"},
    )

    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def create_demo_post():
    """Send a demo POST request and return the parsed response."""
    payload = json.dumps(
        {
            "title": "Week 03 demo",
            "body": "Learning API integration",
            "userId": 1,
        }
    ).encode("utf-8")

    request = Request(
        "https://jsonplaceholder.typicode.com/posts",
        data=payload,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Run a small GET/POST demonstration."""
    try:
        post = fetch_post(1)
        print("Fetched post title:", post["title"])

        created_post = create_demo_post()
        print("Created post ID:", created_post["id"])
    except Exception as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()

"""
Explore a public GitHub endpoint and print a small summary.
"""

import json
from urllib.request import Request, urlopen


def fetch_public_events():
    """Fetch recent public GitHub events and return parsed JSON."""
    request = Request(
        "https://api.github.com/events",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-engineer-week-03-demo",
        },
    )

    with urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Fetch events and print a short summary."""
    try:
        events = fetch_public_events()
        print("Recent GitHub public events:")

        for event in events[:5]:
            event_type = event.get("type", "unknown")
            repo_name = event.get("repo", {}).get("name", "unknown")
            print(f"- {event_type} -> {repo_name}")
    except Exception as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()

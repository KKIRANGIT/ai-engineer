"""
Week 03 - Query Parameters: Building URLs Safely

What this file teaches:
- how query parameters become part of a URL
- why URL encoding matters
- how to keep URL building explicit
"""

from urllib.parse import urlencode


def build_search_url(base_url, params):
    """Return a full URL with encoded query parameters."""
    query_string = urlencode(params)
    return f"{base_url}?{query_string}"


def show_example():
    """Demonstrate query parameter encoding."""
    base_url = "https://api.github.com/search/repositories"
    params = {
        "q": "python requests",
        "sort": "stars",
        "per_page": 5,
    }

    full_url = build_search_url(base_url, params)
    print("Full URL:", full_url)


if __name__ == "__main__":
    show_example()

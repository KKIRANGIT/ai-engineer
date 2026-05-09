"""
Low-level HTTP helpers for the Week 03 GitHub client.
"""

import json
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class ApiError(Exception):
    """Represent an HTTP error response from an API."""

    def __init__(self, status_code, message, body_preview=""):
        super().__init__(message)
        self.status_code = status_code
        self.body_preview = body_preview


class NetworkError(Exception):
    """Represent a transport-level failure such as DNS or timeout issues."""


@dataclass
class JsonResponse:
    """Represent a parsed JSON response plus selected metadata."""

    status_code: int
    headers: dict[str, str]
    json_body: object


def build_url(base_url, path, params=None):
    """Return a full URL, adding query parameters only when provided."""
    normalized_path = path if path.startswith("/") else f"/{path}"
    full_url = f"{base_url}{normalized_path}"

    if not params:
        return full_url

    return f"{full_url}?{urlencode(params)}"


def build_github_headers(token=None):
    """Return the default headers used for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ai-engineer-week-03-client",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def fetch_json(url, headers=None, timeout=10):
    """Send a GET request and return parsed JSON response data."""
    request = Request(url, headers=headers or {})

    try:
        with urlopen(request, timeout=timeout) as response:
            response_body = response.read().decode("utf-8")
            parsed_json = json.loads(response_body)
            response_headers = dict(response.headers.items())

            return JsonResponse(
                status_code=response.status,
                headers=response_headers,
                json_body=parsed_json,
            )
    except HTTPError as error:
        body_preview = error.read().decode("utf-8", errors="replace")
        raise ApiError(
            status_code=error.code,
            message=f"API returned status code {error.code}.",
            body_preview=body_preview[:300],
        ) from error
    except URLError as error:
        raise NetworkError(f"Network request failed: {error.reason}") from error


def parse_link_header(header_value):
    """Parse a GitHub-style Link header into a relation-to-URL dictionary."""
    if not header_value:
        return {}

    parsed_links = {}

    for part in header_value.split(","):
        section = part.strip()
        url_part, rel_part = section.split(";")
        clean_url = url_part.strip()[1:-1]
        relation = rel_part.split("=")[1].strip().strip('"')
        parsed_links[relation] = clean_url

    return parsed_links

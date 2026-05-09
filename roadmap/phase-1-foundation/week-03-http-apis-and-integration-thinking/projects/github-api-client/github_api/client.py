"""
Reusable GitHub API wrapper for Week 03.
"""

from github_api.config import BASE_URL, DEFAULT_TIMEOUT_SECONDS, get_github_token
from github_api.http_utils import (
    build_github_headers,
    build_url,
    fetch_json,
    parse_link_header,
)
from github_api.models import RateLimitSummary, RepoSummary, UserProfile


class GitHubApiClient:
    """Small wrapper around selected GitHub REST API operations."""

    def __init__(self, token=None, timeout=DEFAULT_TIMEOUT_SECONDS):
        self.token = token or get_github_token()
        self.timeout = timeout

    def _headers(self):
        """Return request headers for this client instance."""
        return build_github_headers(self.token)

    def get_user_profile(self, username):
        """Fetch one GitHub user profile and return a UserProfile object."""
        url = build_url(BASE_URL, f"/users/{username}")
        response = fetch_json(url, headers=self._headers(), timeout=self.timeout)
        return UserProfile.from_api_response(response.json_body)

    def list_user_repos(self, username, per_page=5, page=1):
        """Fetch one page of repositories for a GitHub user."""
        url = build_url(
            BASE_URL,
            f"/users/{username}/repos",
            params={"per_page": per_page, "page": page, "sort": "updated"},
        )
        response = fetch_json(url, headers=self._headers(), timeout=self.timeout)
        repos = [RepoSummary.from_api_response(item) for item in response.json_body]
        pagination_links = parse_link_header(response.headers.get("Link", ""))
        return repos, pagination_links

    def get_rate_limit_summary(self):
        """Fetch GitHub rate-limit metadata from the rate limit endpoint."""
        url = build_url(BASE_URL, "/rate_limit")
        response = fetch_json(url, headers=self._headers(), timeout=self.timeout)
        return RateLimitSummary.from_response_headers(response.headers)

"""
Data models for selected GitHub API responses.
"""

from dataclasses import dataclass


@dataclass
class UserProfile:
    """Represent the small slice of GitHub user data this project needs."""

    login: str
    name: str | None
    public_repos: int
    followers: int
    following: int
    profile_url: str
    bio: str | None

    @classmethod
    def from_api_response(cls, raw_data):
        """Build a user profile from one GitHub API response dictionary."""
        if not isinstance(raw_data, dict):
            raise ValueError("User response must be a dictionary.")

        login = raw_data.get("login")
        profile_url = raw_data.get("html_url")

        if not isinstance(login, str) or not login.strip():
            raise ValueError("User response is missing a valid login.")

        if not isinstance(profile_url, str) or not profile_url.strip():
            raise ValueError("User response is missing a valid profile URL.")

        return cls(
            login=login,
            name=raw_data.get("name"),
            public_repos=int(raw_data.get("public_repos", 0)),
            followers=int(raw_data.get("followers", 0)),
            following=int(raw_data.get("following", 0)),
            profile_url=profile_url,
            bio=raw_data.get("bio"),
        )


@dataclass
class RepoSummary:
    """Represent the small slice of repository data this project needs."""

    name: str
    private: bool
    language: str | None
    stars: int
    repo_url: str
    description: str | None

    @classmethod
    def from_api_response(cls, raw_data):
        """Build a repository summary from one GitHub API response dictionary."""
        if not isinstance(raw_data, dict):
            raise ValueError("Repository response must be a dictionary.")

        name = raw_data.get("name")
        repo_url = raw_data.get("html_url")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Repository response is missing a valid name.")

        if not isinstance(repo_url, str) or not repo_url.strip():
            raise ValueError("Repository response is missing a valid repository URL.")

        return cls(
            name=name,
            private=bool(raw_data.get("private", False)),
            language=raw_data.get("language"),
            stars=int(raw_data.get("stargazers_count", 0)),
            repo_url=repo_url,
            description=raw_data.get("description"),
        )


@dataclass
class RateLimitSummary:
    """Represent a small, useful view of the GitHub core rate limit."""

    limit: int
    remaining: int
    used: int

    @classmethod
    def from_response_headers(cls, headers):
        """Build a rate-limit summary from GitHub response headers."""
        return cls(
            limit=int(headers.get("X-RateLimit-Limit", 0)),
            remaining=int(headers.get("X-RateLimit-Remaining", 0)),
            used=int(headers.get("X-RateLimit-Used", 0)),
        )

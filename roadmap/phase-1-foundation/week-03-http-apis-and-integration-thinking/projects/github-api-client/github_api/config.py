"""
Configuration helpers for the Week 03 GitHub client.
"""

import os

BASE_URL = "https://api.github.com"
TOKEN_ENV_NAME = "GITHUB_TOKEN"
DEFAULT_TIMEOUT_SECONDS = 10


def get_github_token():
    """Return the GitHub token from the environment when available."""
    token = os.getenv(TOKEN_ENV_NAME, "").strip()
    return token or None

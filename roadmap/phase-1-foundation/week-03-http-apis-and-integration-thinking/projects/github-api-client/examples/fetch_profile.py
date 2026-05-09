"""
Example script that fetches and prints a small GitHub profile summary.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from github_api.client import GitHubApiClient
from github_api.http_utils import ApiError, NetworkError


def main():
    """Run a simple profile fetch example."""
    client = GitHubApiClient()

    try:
        user_profile = client.get_user_profile("octocat")
        print("Login:", user_profile.login)
        print("Name:", user_profile.name)
        print("Public repos:", user_profile.public_repos)
        print("Profile URL:", user_profile.profile_url)
    except (ApiError, NetworkError, ValueError) as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()

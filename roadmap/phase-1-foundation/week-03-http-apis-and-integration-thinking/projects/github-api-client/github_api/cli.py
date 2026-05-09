"""
CLI entry point for the Week 03 GitHub API client.
"""

from github_api.client import GitHubApiClient
from github_api.http_utils import ApiError, NetworkError


def show_menu():
    """Display the actions available in the CLI."""
    print("\n--- GitHub API Client ---")
    print("1. Fetch user profile")
    print("2. List user repositories")
    print("3. Show rate-limit summary")
    print("4. Exit")


def print_user_profile(user_profile):
    """Print selected fields from a user profile."""
    print(f"\nLogin: {user_profile.login}")
    print(f"Name: {user_profile.name}")
    print(f"Public repos: {user_profile.public_repos}")
    print(f"Followers: {user_profile.followers}")
    print(f"Following: {user_profile.following}")
    print(f"Profile URL: {user_profile.profile_url}")


def print_repositories(repositories):
    """Print a readable list of repository summaries."""
    if not repositories:
        print("\nNo repositories returned.")
        return

    print("\nRepositories:")
    for repository in repositories:
        print(
            f"- {repository.name} | "
            f"Language: {repository.language} | "
            f"Stars: {repository.stars}"
        )


def main():
    """Run the CLI loop."""
    client = GitHubApiClient()

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        try:
            if choice == "1":
                username = input("Enter GitHub username: ").strip()
                user_profile = client.get_user_profile(username)
                print_user_profile(user_profile)

            elif choice == "2":
                username = input("Enter GitHub username: ").strip()
                repositories, pagination_links = client.list_user_repos(username)
                print_repositories(repositories)
                print("Pagination links:", pagination_links)

            elif choice == "3":
                rate_limit = client.get_rate_limit_summary()
                print(
                    f"Limit: {rate_limit.limit}, "
                    f"Remaining: {rate_limit.remaining}, "
                    f"Used: {rate_limit.used}"
                )

            elif choice == "4":
                print("Goodbye. Keep making integrations boring and clear.")
                break

            else:
                print("Invalid option. Choose a number from 1 to 4.")

        except (ApiError, NetworkError, ValueError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

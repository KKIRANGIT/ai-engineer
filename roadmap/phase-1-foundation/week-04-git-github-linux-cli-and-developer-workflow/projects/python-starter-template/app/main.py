"""
CLI entry point for the starter template.
"""

from app.greeter import build_greeting


def main():
    """Prompt for a name and print a greeting."""
    name = input("Enter your name: ")

    try:
        print(build_greeting(name))
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

"""
This exercise shows why context packing is not just "include everything."
"""


def main():
    options = [
        {
            "name": "Overpacked context",
            "effect": "higher coverage, lower focus, more noise",
        },
        {
            "name": "Focused context",
            "effect": "less noise, better answer precision, easier citation tracing",
        },
    ]

    for option in options:
        print(option)


if __name__ == "__main__":
    main()

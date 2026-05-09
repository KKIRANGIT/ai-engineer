"""
Small sample file for Git practice.

This file is intentionally simple because the point of the sandbox is workflow practice,
not application complexity.
"""


def load_sample_tasks():
    """Return a small set of practice tasks."""
    return [
        "Review git status often",
        "Commit related changes together",
        "Use a feature branch for meaningful work",
    ]


def print_tasks():
    """Print the sample tasks in a readable format."""
    for index, task in enumerate(load_sample_tasks(), start=1):
        print(f"{index}. {task}")


if __name__ == "__main__":
    print_tasks()

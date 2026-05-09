"""
Small module used to demonstrate a clean starter layout.
"""

import os


def get_greeting_prefix():
    """Read the greeting prefix from the environment with a safe default."""
    return os.getenv("APP_GREETING_PREFIX", "Hello")


def build_greeting(name):
    """Return a simple greeting string."""
    clean_name = name.strip()

    if not clean_name:
        raise ValueError("Name cannot be empty.")

    prefix = get_greeting_prefix()
    return f"{prefix}, {clean_name}!"

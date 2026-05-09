"""Show that not every failure should be retried blindly."""

from __future__ import annotations


def main() -> None:
    print("Timeouts may justify a retry.")
    print("High-risk injection patterns should usually block rather than retry.")


if __name__ == "__main__":
    main()

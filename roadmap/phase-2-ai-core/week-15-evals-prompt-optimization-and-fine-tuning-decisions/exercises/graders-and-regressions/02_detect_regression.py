"""Show how one improved metric can still hide a regression elsewhere."""

from __future__ import annotations


def main() -> None:
    before = {"category": 4, "tone": 2}
    after = {"category": 4, "tone": 4}
    regression = {"category": 3, "tone": 5}

    print("Improvement:", after)
    print("Hidden regression example:", regression)
    print("Always inspect case-level failures, not only averages.")


if __name__ == "__main__":
    main()

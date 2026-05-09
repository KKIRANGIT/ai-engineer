"""CLI entry points for the Week 17 guarded assistant lab."""

from __future__ import annotations

import argparse

from .case_loader import load_cases
from .processor import run_case


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 17 guarded support assistant lab.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run one request case.")
    run_parser.add_argument("--case", dest="case_id", required=True)

    subparsers.add_parser("list-cases", help="List available request cases.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list-cases":
        for case in load_cases():
            print(f"- {case.case_id}: {case.expected_risk}")
        return

    result = run_case(args.case_id)
    print(f"Case: {result.case_id}")
    print(f"Risk level: {result.risk_level}")
    print(f"Blocked: {result.blocked}")
    print(f"Estimated cost: {result.estimated_cost}")
    print(f"Response: {result.response_text}")
    print(f"Trace file: {result.trace_path}")


if __name__ == "__main__":
    main()

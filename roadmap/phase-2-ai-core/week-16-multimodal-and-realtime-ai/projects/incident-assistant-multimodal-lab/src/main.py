"""CLI entry points for the Week 16 multimodal lab."""

from __future__ import annotations

import argparse

from .case_loader import load_cases
from .session import run_case


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 16 incident assistant multimodal lab.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run one incident case.")
    run_parser.add_argument("--case", dest="case_id", required=True)
    run_parser.add_argument("--mode", choices=["text", "multimodal", "session"], required=True)

    subparsers.add_parser("list-cases", help="List available incident cases.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list-cases":
        for case in load_cases():
            print(f"- {case.case_id}: {case.title}")
        return

    result = run_case(args.case_id, args.mode)
    print(result.summary)
    print("\nStreamed chunks:")
    for chunk in result.streamed_chunks:
        print(f"[chunk] {chunk}")
    print(f"\nTrace file: {result.trace_path}")


if __name__ == "__main__":
    main()

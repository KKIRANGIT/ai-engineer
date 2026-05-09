"""Command-line entry points for the Week 13 tool-calling lab."""

from __future__ import annotations

import argparse
import json

from .assistant import OperationsAssistant
from .providers import build_anthropic_tools_payload, build_openai_tools_payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 13 tool-use and function-calling lab.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run the local assistant against a query.")
    run_parser.add_argument("--query", required=True, help="User query for the assistant.")

    subparsers.add_parser("show-openai-tools", help="Print OpenAI tool payloads.")
    subparsers.add_parser("show-anthropic-tools", help="Print Anthropic tool payloads.")
    subparsers.add_parser("show-sample-queries", help="Print useful sample queries.")

    return parser


def print_json(data: object) -> None:
    print(json.dumps(data, indent=2))


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        assistant = OperationsAssistant()
        result = assistant.run(args.query)

        print("Planned calls:")
        for call in result.planned_calls:
            print(f"- {call.name}: {call.arguments} ({call.reason})")

        print("\nFinal answer:\n")
        print(result.final_answer)
        print(f"\nTrace file: {result.trace_path}")
        return

    if args.command == "show-openai-tools":
        print_json(build_openai_tools_payload())
        return

    if args.command == "show-anthropic-tools":
        print_json(build_anthropic_tools_payload())
        return

    if args.command == "show-sample-queries":
        samples = [
            "Look up ticket T-1001 and summarize the issue.",
            "Search the refund policy and tell me the main rule.",
            "What is 35 percent of 1200?",
            "What is the weather in Bengaluru?",
            "Look up ticket T-1002, search the refund policy, and calculate 50 percent of 1200.",
        ]
        print_json(samples)


if __name__ == "__main__":
    main()

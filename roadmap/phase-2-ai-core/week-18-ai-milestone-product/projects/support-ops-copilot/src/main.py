"""CLI entry points for the Week 18 capstone project."""

from __future__ import annotations

import argparse
import json

from .analyzer import analyze_ticket
from .case_loader import load_tickets
from .evals import run_eval


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 18 support ops copilot.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Analyze one ticket.")
    run_parser.add_argument("--ticket", dest="ticket_id", required=True)

    subparsers.add_parser("list-tickets", help="List available tickets.")
    subparsers.add_parser("evaluate", help="Run the milestone eval set.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "list-tickets":
        for ticket in load_tickets():
            print(f"- {ticket.ticket_id}: {ticket.title}")
        return

    if args.command == "evaluate":
        print(json.dumps(run_eval(), indent=2))
        return

    output = analyze_ticket(args.ticket_id)
    print(json.dumps(output.to_dict(), indent=2))


if __name__ == "__main__":
    main()

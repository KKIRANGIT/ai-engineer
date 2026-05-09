import argparse
import json
from dataclasses import asdict
from pprint import pprint

from src import config
from src.mock_engine import classify_ticket
from src.openai_structured_client import build_openai_structured_payload, call_openai_structured_output
from src.prompt_library import get_ticket_by_id, render_prompt
from src.regression import run_mock_regression
from src.validators import load_schema, validate_structured_output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 10 Support Ticket Triage Lab")
    subparsers = parser.add_subparsers(dest="command", required=True)

    prompt_parser = subparsers.add_parser("show-prompt")
    prompt_parser.add_argument("--template", required=True)
    prompt_parser.add_argument("--ticket-id", required=True)

    request_parser = subparsers.add_parser("show-request")
    request_parser.add_argument("--template", required=True)
    request_parser.add_argument("--ticket-id", required=True)

    run_parser = subparsers.add_parser("run-case")
    run_parser.add_argument("--mode", choices=["mock", "openai"], required=True)
    run_parser.add_argument("--template", required=True)
    run_parser.add_argument("--ticket-id", required=True)

    regress_parser = subparsers.add_parser("regress")
    regress_parser.add_argument("--mode", choices=["mock"], required=True)
    regress_parser.add_argument("--template", required=True)

    return parser


def show_prompt(template_name: str, ticket_id: str) -> None:
    ticket = get_ticket_by_id(ticket_id)
    print(render_prompt(template_name, ticket.text))


def show_request(template_name: str, ticket_id: str) -> None:
    ticket = get_ticket_by_id(ticket_id)
    prompt_text = render_prompt(template_name, ticket.text)
    payload = build_openai_structured_payload(config.get_openai_model(), prompt_text, load_schema())
    print(json.dumps(payload, indent=2))


def run_case(mode: str, template_name: str, ticket_id: str) -> None:
    ticket = get_ticket_by_id(ticket_id)
    prompt_text = render_prompt(template_name, ticket.text)

    if mode == "mock":
        result = asdict(classify_ticket(ticket))
    else:
        result = call_openai_structured_output(config.get_openai_model(), prompt_text, load_schema())

    if "refusal" in result:
        pprint(result)
        return

    validate_structured_output(result)
    pprint(result)


def run_regression() -> None:
    outcomes = run_mock_regression()
    passed = 0

    for outcome in outcomes:
        status = "PASS" if outcome.passed else "FAIL"
        print(f"{status} - {outcome.ticket_id}")
        if outcome.failures:
            for failure in outcome.failures:
                print(f"  - {failure}")
        else:
            passed += 1

    print(f"\nRegression summary: {passed}/{len(outcomes)} cases passed.")


def main() -> None:
    parser = build_parser()
    arguments = parser.parse_args()

    if arguments.command == "show-prompt":
        show_prompt(arguments.template, arguments.ticket_id)
    elif arguments.command == "show-request":
        show_request(arguments.template, arguments.ticket_id)
    elif arguments.command == "run-case":
        run_case(arguments.mode, arguments.template, arguments.ticket_id)
    elif arguments.command == "regress":
        run_regression()


if __name__ == "__main__":
    main()

import argparse
from dataclasses import asdict
from pprint import pprint

from src.debug_tools import build_debug_view
from src.evaluation import run_evaluation
from src.rag_pipeline import GroundedPolicyAssistant


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 12 Grounded Policy Assistant")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ask_parser = subparsers.add_parser("ask")
    ask_parser.add_argument("--question", required=True)
    ask_parser.add_argument("--debug", action="store_true")

    subparsers.add_parser("evaluate")

    return parser


def main() -> None:
    parser = build_parser()
    arguments = parser.parse_args()

    if arguments.command == "ask":
        assistant = GroundedPolicyAssistant()
        answer = assistant.answer(arguments.question)
        pprint(asdict(answer))
        if arguments.debug:
            print("\nDEBUG VIEW:")
            pprint(build_debug_view(answer))
        return

    if arguments.command == "evaluate":
        outcomes = run_evaluation()
        passed = 0
        for outcome in outcomes:
            status = "PASS" if outcome["passed"] else "FAIL"
            print(f"{status} - {outcome['question']}")
            print(
                {
                    "expected_document_id": outcome["expected_document_id"],
                    "retrieved_document_id": outcome["retrieved_document_id"],
                }
            )
            if outcome["passed"]:
                passed += 1
        print(f"\nEvaluation summary: {passed}/{len(outcomes)} questions passed.")


if __name__ == "__main__":
    main()

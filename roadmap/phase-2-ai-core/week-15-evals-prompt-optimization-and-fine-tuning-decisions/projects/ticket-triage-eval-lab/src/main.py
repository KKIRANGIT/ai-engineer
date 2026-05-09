"""CLI entry points for the Week 15 eval lab."""

from __future__ import annotations

import argparse
import json

from .analysis import compare_variants, run_variant, summarize_scores
from .decision_memo import generate_decision_memo
from .report import write_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 15 ticket triage eval lab.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run one evaluation variant.")
    run_parser.add_argument("--variant", choices=["baseline", "prompt_v2", "retrieval_v1"], required=True)

    subparsers.add_parser("compare", help="Compare all variants.")
    subparsers.add_parser("memo", help="Generate the optimization decision memo.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        scores = run_variant(args.variant)
        summary = summarize_scores(scores)
        payload = {
            "variant": args.variant,
            "summary": summary,
            "case_scores": [score.to_dict() for score in scores],
        }
        path = write_report(f"{args.variant}_report.json", payload)
        print(json.dumps(summary, indent=2))
        print(f"\nReport file: {path}")
        return

    if args.command == "compare":
        result = compare_variants(["baseline", "prompt_v2", "retrieval_v1"])
        path = write_report("comparison_report.json", result)
        print(json.dumps(result, indent=2))
        print(f"\nReport file: {path}")
        return

    memo = generate_decision_memo()
    path = write_report("decision_memo.json", {"memo": memo})
    print(memo)
    print(f"\nReport file: {path}")


if __name__ == "__main__":
    main()

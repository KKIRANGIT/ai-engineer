"""CLI entry points for the Week 14 orchestration project."""

from __future__ import annotations

import argparse
from pathlib import Path

from .agent_loop import run_agent_loop
from .data_access import DocumentStore
from .direct_workflow import run_direct_workflow
from .graph_workflow import run_graph_workflow
from .models import RunResult, WorkflowState
from .traces import TraceRecorder


TRACE_PATH = Path("artifacts/latest_trace.json")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Week 14 research brief orchestrator.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run one orchestration mode.")
    run_parser.add_argument("--mode", choices=["direct", "graph", "agent"], required=True)
    run_parser.add_argument("--query", required=True)

    subparsers.add_parser("show-sample-queries", help="Print useful sample queries.")
    return parser


def execute_mode(mode: str, query: str, store: DocumentStore) -> WorkflowState:
    if mode == "direct":
        return run_direct_workflow(query, store)
    if mode == "graph":
        return run_graph_workflow(query, store)
    if mode == "agent":
        return run_agent_loop(query, store)
    raise ValueError(f"Unsupported mode: {mode}")


def run(mode: str, query: str) -> RunResult:
    store = DocumentStore()
    recorder = TraceRecorder()
    state = execute_mode(mode, query, store)

    for step in state.step_history:
        recorder.record(step.stage, step.details)

    recorder.record(
        "final_state",
        {
            "needs_human_review": state.needs_human_review,
            "brief": state.brief,
        },
    )
    recorder.save(TRACE_PATH)

    return RunResult(
        mode=mode,
        final_brief=state.brief,
        needs_human_review=state.needs_human_review,
        trace_path=str(TRACE_PATH),
        state=state,
    )


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "show-sample-queries":
        for query in [
            "Prepare a brief about refund policy for enterprise customers.",
            "Summarize travel reimbursement and security requirements.",
            "Create a brief about laptop requests and refund exceptions.",
            "Explain password reset and MFA requirements.",
        ]:
            print(f"- {query}")
        return

    result = run(args.mode, args.query)
    print(f"Mode: {result.mode}")
    print(f"Needs human review: {result.needs_human_review}")
    print("\nFinal brief:\n")
    print(result.final_brief)
    print(f"\nTrace file: {result.trace_path}")


if __name__ == "__main__":
    main()

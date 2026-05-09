"""Assistant orchestration for the Week 13 tool-calling lab."""

from __future__ import annotations

from pathlib import Path

from .data_access import WorkspaceDataStore
from .models import AssistantResult, ToolCall, ToolOutcome
from .planner import RuleBasedPlanner
from .tools import execute_tool
from .traces import TraceRecorder
from .validators import ValidationError, validate_tool_arguments


class OperationsAssistant:
    """Run the local plan -> validate -> execute -> summarize loop."""

    def __init__(self, store: WorkspaceDataStore | None = None, trace_path: Path | None = None) -> None:
        self.store = store or WorkspaceDataStore()
        self.planner = RuleBasedPlanner()
        self.trace_path = trace_path or Path("artifacts/latest_trace.json")

    def run(self, user_query: str) -> AssistantResult:
        recorder = TraceRecorder()
        planned_calls = self.planner.plan(user_query)
        recorder.record(
            "planning",
            {
                "user_query": user_query,
                "planned_calls": [call.to_dict() for call in planned_calls],
            },
        )

        outcomes: list[ToolOutcome] = []

        for call in planned_calls:
            outcome = self._handle_call(call, recorder)
            outcomes.append(outcome)

        final_answer = self._compose_final_answer(user_query, planned_calls, outcomes)
        recorder.record("final_answer", {"text": final_answer})
        recorder.save(self.trace_path)

        return AssistantResult(
            user_query=user_query,
            planned_calls=planned_calls,
            outcomes=outcomes,
            final_answer=final_answer,
            trace_path=str(self.trace_path),
        )

    def _handle_call(self, call: ToolCall, recorder: TraceRecorder) -> ToolOutcome:
        try:
            validated_arguments = validate_tool_arguments(call.name, call.arguments)
            recorder.record(
                "validation_passed",
                {"tool_name": call.name, "arguments": validated_arguments},
            )
        except ValidationError as error:
            recorder.record(
                "validation_failed",
                {"tool_name": call.name, "arguments": call.arguments, "error": str(error)},
            )
            return ToolOutcome(
                name=call.name,
                arguments=call.arguments,
                ok=False,
                error=str(error),
            )

        output = execute_tool(self.store, call.name, validated_arguments)
        recorder.record(
            "tool_executed",
            {"tool_name": call.name, "arguments": validated_arguments, "output": output},
        )
        return ToolOutcome(name=call.name, arguments=validated_arguments, ok=True, output=output)

    def _compose_final_answer(
        self,
        user_query: str,
        planned_calls: list[ToolCall],
        outcomes: list[ToolOutcome],
    ) -> str:
        if not planned_calls:
            return (
                "No tool call was planned for this query. Try asking for a ticket lookup, policy search, "
                "refund calculation, or weather snapshot."
            )

        lines = [f"User query: {user_query}", "", "Assistant summary:"]

        for outcome in outcomes:
            if not outcome.ok:
                lines.append(f"- {outcome.name}: validation failed -> {outcome.error}")
                continue

            lines.append(self._render_success(outcome))

        return "\n".join(lines)

    def _render_success(self, outcome: ToolOutcome) -> str:
        output = outcome.output or {}

        if outcome.name == "lookup_ticket":
            if not output.get("found"):
                return f"- lookup_ticket: {output['message']}"
            ticket = output["ticket"]
            return (
                f"- lookup_ticket: {ticket['ticket_id']} is '{ticket['summary']}' with status "
                f"{ticket['status']}, priority {ticket['priority']}, and owner {ticket['owner']}."
            )

        if outcome.name == "search_policy_docs":
            if not output.get("found"):
                return f"- search_policy_docs: no policy match found for '{output['query']}'."
            titles = ", ".join(match["title"] for match in output["matches"])
            return f"- search_policy_docs: matched policy documents -> {titles}."

        if outcome.name == "calculate_refund":
            return (
                f"- calculate_refund: {output['percent']}% of {output['amount']} is {output['refund_value']}. "
                f"Remaining amount is {output['remaining_amount']}."
            )

        if outcome.name == "get_weather_snapshot":
            if not output.get("found"):
                return f"- get_weather_snapshot: {output['message']}"
            snapshot = output["snapshot"]
            return (
                f"- get_weather_snapshot: {snapshot['city']} is {snapshot['condition']} at "
                f"{snapshot['temperature_c']}C with humidity {snapshot['humidity_percent']}%."
            )

        return f"- {outcome.name}: completed."

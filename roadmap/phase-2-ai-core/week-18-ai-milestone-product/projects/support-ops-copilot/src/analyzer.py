"""Integrated ticket analysis workflow for the Week 18 capstone."""

from __future__ import annotations

from pathlib import Path

from .case_loader import get_ticket
from .cost import estimate_cost
from .guardrails import screen_ticket
from .models import AnalysisOutput
from .retrieval import infer_category, retrieve_policy_notes
from .tools import calculate_sla_hours, decide_priority, should_escalate
from .traces import TraceRecorder


TRACE_PATH = Path("artifacts/latest_trace.json")


def analyze_ticket(ticket_id: str) -> AnalysisOutput:
    ticket = get_ticket(ticket_id)
    recorder = TraceRecorder()
    recorder.record("ticket_loaded", ticket.to_dict())

    safe, findings = screen_ticket(ticket)
    recorder.record("guardrail_check", {"safe": safe, "findings": findings})
    if not safe:
        response_text = "Ticket blocked for manual review due to suspicious instruction content."
        cost_estimate = estimate_cost(f"{ticket.title} {ticket.body}", response_text)
        recorder.record("blocked", {"response_text": response_text, "cost_estimate": cost_estimate})
        recorder.save(TRACE_PATH)
        return AnalysisOutput(
            ticket_id=ticket.ticket_id,
            category="manual_review",
            priority="high",
            recommended_action=response_text,
            source_titles=[],
            sla_hours=0,
            escalation_needed=True,
            cost_estimate=cost_estimate,
        )

    category = infer_category(ticket)
    policy_notes = retrieve_policy_notes(ticket)
    recorder.record("retrieval", {"category": category, "source_titles": [note.title for note in policy_notes]})

    priority = decide_priority(category, f"{ticket.title} {ticket.body}")
    sla_hours = calculate_sla_hours(priority, ticket.customer_tier)
    escalation_needed = should_escalate(category, priority, ticket.customer_tier)

    source_titles = [note.title for note in policy_notes]
    recommended_action = (
        f"Classify as {category}. Route with {priority} priority. "
        f"Use {sla_hours}-hour SLA and {'escalate' if escalation_needed else 'standard handling'} path."
    )

    cost_estimate = estimate_cost(
        f"{ticket.title} {ticket.body} {' '.join(note.summary for note in policy_notes)}",
        recommended_action,
    )
    recorder.record(
        "analysis_complete",
        {
            "category": category,
            "priority": priority,
            "sla_hours": sla_hours,
            "escalation_needed": escalation_needed,
            "cost_estimate": cost_estimate,
        },
    )
    recorder.save(TRACE_PATH)

    return AnalysisOutput(
        ticket_id=ticket.ticket_id,
        category=category,
        priority=priority,
        recommended_action=recommended_action,
        source_titles=source_titles,
        sla_hours=sla_hours,
        escalation_needed=escalation_needed,
        cost_estimate=cost_estimate,
    )

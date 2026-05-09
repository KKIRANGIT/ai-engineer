"""Local system variants used for Week 15 evaluation."""

from __future__ import annotations

from .models import EvalCase, SystemOutput
from .retrieval_knowledge import lookup_policy_hint


def _infer_category(ticket_text: str) -> str:
    text = ticket_text.lower()
    if "refund" in text or "duplicate charge" in text:
        return "refund"
    if "receipt" in text or "travel" in text or "hotel" in text:
        return "travel"
    if "password" in text or "mfa" in text or "security" in text:
        return "security"
    if "invoice" in text or "billing" in text:
        return "billing"
    return "general"


def _infer_priority(ticket_text: str) -> str:
    text = ticket_text.lower()
    if "locked out" in text or "urgent" in text or "cannot access" in text:
        return "high"
    if "today" in text or "soon" in text:
        return "medium"
    return "low"


def run_system(case: EvalCase, variant: str) -> SystemOutput:
    category = _infer_category(case.ticket_text)
    priority = _infer_priority(case.ticket_text)

    if variant == "baseline":
        next_action = f"Route to {category} queue"
        customer_reply = (
            f"We received your request. The issue appears related to {category}. "
            f"Our team will review it."
        )
        return SystemOutput(category=category, priority=priority, next_action=next_action, customer_reply=customer_reply)

    if variant == "prompt_v2":
        next_action = f"Route to {category} queue and acknowledge expected process"
        customer_reply = (
            f"Thanks for the details. We identified this as a {category} issue with {priority} priority. "
            f"Our next step is to review the case and share a clear update."
        )
        return SystemOutput(category=category, priority=priority, next_action=next_action, customer_reply=customer_reply)

    if variant == "retrieval_v1":
        hint = lookup_policy_hint(category)
        next_action = f"Route to {category} queue and reference policy guidance"
        reply = (
            f"Thanks for the details. We identified this as a {category} issue with {priority} priority. "
            f"Our next step is to review the case and share a clear update."
        )
        if hint:
            reply += f" Relevant policy guidance: {hint}."
        return SystemOutput(category=category, priority=priority, next_action=next_action, customer_reply=reply)

    raise ValueError(f"Unknown system variant: {variant}")

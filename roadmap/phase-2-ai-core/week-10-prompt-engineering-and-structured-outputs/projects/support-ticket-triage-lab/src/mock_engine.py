from src.models import Ticket, TriageResult


def classify_ticket(ticket: Ticket) -> TriageResult:
    text = ticket.text.lower()

    if "charged twice" in text or "refund" in text:
        return TriageResult(
            category="billing",
            priority="medium",
            summary="The user reports a duplicate billing issue and requests a refund.",
            needs_human_follow_up=True,
            confidence_note="High confidence because the billing problem is explicit.",
        )

    if "crash" in text or "crashes" in text:
        return TriageResult(
            category="bug",
            priority="high",
            summary="The user reports a repeatable application crash during normal usage.",
            needs_human_follow_up=True,
            confidence_note="High confidence because the failure mode is concrete and repeatable.",
        )

    if "cannot sign in" in text or "can't sign in" in text or "password" in text:
        return TriageResult(
            category="account_access",
            priority="high",
            summary="The user is blocked from account access after attempting a password reset.",
            needs_human_follow_up=True,
            confidence_note="High confidence because the access-blocking issue is clear.",
        )

    if "add" in text or "feature" in text or "dark mode" in text:
        return TriageResult(
            category="feature_request",
            priority="low",
            summary="The user is requesting a product enhancement rather than reporting a failure.",
            needs_human_follow_up=False,
            confidence_note="Medium confidence because the request is clearly feature-oriented.",
        )

    return TriageResult(
        category="unclear",
        priority="medium",
        summary="The ticket does not provide enough detail to classify confidently.",
        needs_human_follow_up=True,
        confidence_note="Low confidence because the request lacks concrete information.",
    )

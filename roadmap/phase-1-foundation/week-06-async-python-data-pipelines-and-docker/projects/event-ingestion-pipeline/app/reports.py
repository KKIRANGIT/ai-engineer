"""
Summary report helpers for the Week 06 pipeline.
"""


def build_summary(cleaned_events):
    """Return high-level counts and totals for the cleaned event set."""
    total_events = len(cleaned_events)
    total_minutes = 0
    total_score = 0
    completed_events = 0

    for event in cleaned_events:
        total_minutes += event.duration_minutes
        total_score += event.score

        if event.status == "done":
            completed_events += 1

    return {
        "total_events": total_events,
        "completed_events": completed_events,
        "total_minutes": total_minutes,
        "total_score": total_score,
    }

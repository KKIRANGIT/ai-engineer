from datetime import date


class ValidationError(Exception):
    def __init__(self, message: str, errors: list[str]) -> None:
        super().__init__(message)
        self.message = message
        self.errors = errors


def validate_subject_payload(payload: dict) -> dict:
    errors = []

    name = payload.get("name")
    category = payload.get("category", "general")
    target_minutes_per_week = payload.get("target_minutes_per_week")

    if not isinstance(name, str) or not name.strip():
        errors.append("name must be a non-empty string")

    if not isinstance(category, str) or not category.strip():
        errors.append("category must be a non-empty string")

    if not isinstance(target_minutes_per_week, int) or target_minutes_per_week <= 0:
        errors.append("target_minutes_per_week must be a positive integer")

    if errors:
        raise ValidationError("Invalid subject payload.", errors)

    return {
        "name": name.strip(),
        "category": category.strip(),
        "target_minutes_per_week": target_minutes_per_week,
    }


def validate_session_payload(payload: dict) -> dict:
    errors = []

    subject_id = payload.get("subject_id")
    session_date = payload.get("session_date")
    duration_minutes = payload.get("duration_minutes")
    focus_score = payload.get("focus_score")
    notes = payload.get("notes", "")

    if not isinstance(subject_id, int) or subject_id <= 0:
        errors.append("subject_id must be a positive integer")

    if not isinstance(session_date, str):
        errors.append("session_date must be a string in YYYY-MM-DD format")
    else:
        try:
            date.fromisoformat(session_date)
        except ValueError:
            errors.append("session_date must be a valid date in YYYY-MM-DD format")

    if not isinstance(duration_minutes, int) or duration_minutes <= 0:
        errors.append("duration_minutes must be a positive integer")

    if not isinstance(focus_score, int) or not 1 <= focus_score <= 5:
        errors.append("focus_score must be an integer between 1 and 5")

    if not isinstance(notes, str):
        errors.append("notes must be a string when provided")

    if errors:
        raise ValidationError("Invalid session payload.", errors)

    return {
        "subject_id": subject_id,
        "session_date": session_date,
        "duration_minutes": duration_minutes,
        "focus_score": focus_score,
        "notes": notes.strip(),
    }

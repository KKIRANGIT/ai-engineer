from src.repository import StudyTrackerRepository
from src.validation import ValidationError, validate_session_payload, validate_subject_payload


class StudyTrackerService:
    def __init__(self, repository: StudyTrackerRepository) -> None:
        self.repository = repository

    def list_subjects(self) -> list[dict]:
        return self.repository.list_subjects()

    def create_subject(self, payload: dict) -> dict:
        cleaned_payload = validate_subject_payload(payload)
        return self.repository.create_subject(**cleaned_payload)

    def list_sessions(self) -> list[dict]:
        return self.repository.list_sessions()

    def create_session(self, payload: dict) -> dict:
        cleaned_payload = validate_session_payload(payload)

        if self.repository.get_subject_by_id(cleaned_payload["subject_id"]) is None:
            raise ValidationError(
                "Invalid session payload.",
                ["subject_id must reference an existing subject"],
            )

        return self.repository.create_session(**cleaned_payload)

    def delete_session(self, session_id: int) -> bool:
        return self.repository.delete_session(session_id)

    def get_summary(self) -> dict:
        summary = self.repository.get_summary()
        summary["subject_count"] = len(self.repository.list_subjects())
        return summary

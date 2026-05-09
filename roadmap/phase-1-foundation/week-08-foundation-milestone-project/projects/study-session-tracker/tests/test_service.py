import tempfile
import unittest
from pathlib import Path

from src.db import initialize_database
from src.repository import StudyTrackerRepository
from src.service import StudyTrackerService
from src.validation import ValidationError


class StudyTrackerServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temp_directory.name) / "service.db"
        initialize_database(self.database_path)
        repository = StudyTrackerRepository(self.database_path)
        self.service = StudyTrackerService(repository)

    def tearDown(self) -> None:
        self.temp_directory.cleanup()

    def test_create_subject_validates_payload(self) -> None:
        with self.assertRaises(ValidationError):
            self.service.create_subject(
                {
                    "name": "",
                    "category": "",
                    "target_minutes_per_week": 0,
                }
            )

    def test_create_session_requires_existing_subject(self) -> None:
        with self.assertRaises(ValidationError):
            self.service.create_session(
                {
                    "subject_id": 999,
                    "session_date": "2026-05-09",
                    "duration_minutes": 45,
                    "focus_score": 4,
                    "notes": "Tried logging without a subject.",
                }
            )

    def test_get_summary_adds_subject_count(self) -> None:
        subject = self.service.create_subject(
            {
                "name": "Node Basics",
                "category": "backend",
                "target_minutes_per_week": 150,
            }
        )
        self.service.create_session(
            {
                "subject_id": subject["id"],
                "session_date": "2026-05-09",
                "duration_minutes": 50,
                "focus_score": 4,
                "notes": "Worked through routing.",
            }
        )

        summary = self.service.get_summary()

        self.assertEqual(summary["subject_count"], 1)
        self.assertEqual(summary["total_sessions"], 1)
        self.assertEqual(summary["total_minutes"], 50)


if __name__ == "__main__":
    unittest.main()

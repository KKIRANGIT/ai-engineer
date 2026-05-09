import tempfile
import unittest
from pathlib import Path

from src.db import initialize_database
from src.repository import StudyTrackerRepository


class StudyTrackerRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_directory = tempfile.TemporaryDirectory()
        self.database_path = Path(self.temp_directory.name) / "test.db"
        initialize_database(self.database_path)
        self.repository = StudyTrackerRepository(self.database_path)

    def tearDown(self) -> None:
        self.temp_directory.cleanup()

    def test_create_subject_and_list_subjects(self) -> None:
        created_subject = self.repository.create_subject("Python", "backend", 240)

        subjects = self.repository.list_subjects()

        self.assertEqual(created_subject["name"], "Python")
        self.assertEqual(len(subjects), 1)
        self.assertEqual(subjects[0]["category"], "backend")

    def test_create_session_and_summary(self) -> None:
        subject = self.repository.create_subject("SQL", "database", 180)
        self.repository.create_session(
            subject_id=subject["id"],
            session_date="2026-05-09",
            duration_minutes=75,
            focus_score=4,
            notes="Worked on joins.",
        )

        sessions = self.repository.list_sessions()
        summary = self.repository.get_summary()

        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0]["subject_name"], "SQL")
        self.assertEqual(summary["total_sessions"], 1)
        self.assertEqual(summary["total_minutes"], 75)

    def test_delete_session_returns_true_when_deleted(self) -> None:
        subject = self.repository.create_subject("APIs", "backend", 200)
        session = self.repository.create_session(
            subject_id=subject["id"],
            session_date="2026-05-09",
            duration_minutes=60,
            focus_score=5,
            notes="Practiced HTTP requests.",
        )

        deleted = self.repository.delete_session(session["id"])

        self.assertTrue(deleted)
        self.assertEqual(self.repository.list_sessions(), [])


if __name__ == "__main__":
    unittest.main()

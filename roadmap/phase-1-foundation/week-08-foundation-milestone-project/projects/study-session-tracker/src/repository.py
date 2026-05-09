from datetime import datetime
from pathlib import Path

from src.db import get_connection


class StudyTrackerRepository:
    def __init__(self, database_path: Path) -> None:
        self.database_path = database_path

    def list_subjects(self) -> list[dict]:
        query = """
        SELECT id, name, category, target_minutes_per_week, created_at
        FROM subjects
        ORDER BY name ASC
        """

        with get_connection(self.database_path) as connection:
            rows = connection.execute(query).fetchall()
            return [dict(row) for row in rows]

    def create_subject(self, name: str, category: str, target_minutes_per_week: int) -> dict:
        query = """
        INSERT INTO subjects (name, category, target_minutes_per_week, created_at)
        VALUES (?, ?, ?, ?)
        """

        created_at = datetime.utcnow().isoformat(timespec="seconds")

        with get_connection(self.database_path) as connection:
            cursor = connection.execute(
                query,
                (name, category, target_minutes_per_week, created_at),
            )
            subject_id = cursor.lastrowid
            connection.commit()

        return self.get_subject_by_id(subject_id)

    def get_subject_by_id(self, subject_id: int) -> dict | None:
        query = """
        SELECT id, name, category, target_minutes_per_week, created_at
        FROM subjects
        WHERE id = ?
        """

        with get_connection(self.database_path) as connection:
            row = connection.execute(query, (subject_id,)).fetchone()
            return dict(row) if row else None

    def create_session(
        self,
        subject_id: int,
        session_date: str,
        duration_minutes: int,
        focus_score: int,
        notes: str,
    ) -> dict:
        query = """
        INSERT INTO study_sessions (
            subject_id,
            session_date,
            duration_minutes,
            focus_score,
            notes,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """

        created_at = datetime.utcnow().isoformat(timespec="seconds")

        with get_connection(self.database_path) as connection:
            cursor = connection.execute(
                query,
                (
                    subject_id,
                    session_date,
                    duration_minutes,
                    focus_score,
                    notes,
                    created_at,
                ),
            )
            session_id = cursor.lastrowid
            connection.commit()

        return self.get_session_by_id(session_id)

    def list_sessions(self) -> list[dict]:
        query = """
        SELECT
            study_sessions.id,
            study_sessions.subject_id,
            study_sessions.session_date,
            study_sessions.duration_minutes,
            study_sessions.focus_score,
            study_sessions.notes,
            study_sessions.created_at,
            subjects.name AS subject_name
        FROM study_sessions
        JOIN subjects ON subjects.id = study_sessions.subject_id
        ORDER BY study_sessions.session_date DESC, study_sessions.id DESC
        """

        with get_connection(self.database_path) as connection:
            rows = connection.execute(query).fetchall()
            return [dict(row) for row in rows]

    def get_session_by_id(self, session_id: int) -> dict | None:
        query = """
        SELECT
            study_sessions.id,
            study_sessions.subject_id,
            study_sessions.session_date,
            study_sessions.duration_minutes,
            study_sessions.focus_score,
            study_sessions.notes,
            study_sessions.created_at,
            subjects.name AS subject_name
        FROM study_sessions
        JOIN subjects ON subjects.id = study_sessions.subject_id
        WHERE study_sessions.id = ?
        """

        with get_connection(self.database_path) as connection:
            row = connection.execute(query, (session_id,)).fetchone()
            return dict(row) if row else None

    def delete_session(self, session_id: int) -> bool:
        query = "DELETE FROM study_sessions WHERE id = ?"

        with get_connection(self.database_path) as connection:
            cursor = connection.execute(query, (session_id,))
            connection.commit()
            return cursor.rowcount > 0

    def get_summary(self) -> dict:
        totals_query = """
        SELECT
            COUNT(*) AS total_sessions,
            COALESCE(SUM(duration_minutes), 0) AS total_minutes
        FROM study_sessions
        """

        by_subject_query = """
        SELECT
            subjects.name AS subject_name,
            COALESCE(SUM(study_sessions.duration_minutes), 0) AS total_minutes
        FROM subjects
        LEFT JOIN study_sessions ON study_sessions.subject_id = subjects.id
        GROUP BY subjects.id, subjects.name
        ORDER BY total_minutes DESC, subjects.name ASC
        """

        with get_connection(self.database_path) as connection:
            totals_row = connection.execute(totals_query).fetchone()
            subject_rows = connection.execute(by_subject_query).fetchall()

        return {
            "total_sessions": totals_row["total_sessions"],
            "total_minutes": totals_row["total_minutes"],
            "minutes_by_subject": [dict(row) for row in subject_rows],
        }

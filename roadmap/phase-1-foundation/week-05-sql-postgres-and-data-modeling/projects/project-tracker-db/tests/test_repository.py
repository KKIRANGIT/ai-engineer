import tempfile
import unittest
from pathlib import Path

from app.db import connect, initialize_database, seed_database
from app.reports import list_project_summaries
from app.repository import (
    add_task,
    create_task_with_tags,
    list_tasks,
    mark_task_done,
)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        db_path = Path(self.temp_dir.name) / "tracker.db"
        self.connection = connect(db_path)
        initialize_database(self.connection)
        seed_database(self.connection)

    def tearDown(self):
        self.connection.close()
        self.temp_dir.cleanup()

    def test_add_task_creates_new_task(self):
        new_task_id = add_task(
            self.connection,
            project_id=1,
            title="Review schema constraints",
            priority=5,
        )

        task_ids = [task.task_id for task in list_tasks(self.connection)]
        self.assertIn(new_task_id, task_ids)

    def test_mark_task_done_updates_status(self):
        new_task_id = add_task(
            self.connection,
            project_id=1,
            title="Review indexing notes",
            priority=4,
        )

        mark_task_done(self.connection, new_task_id)

        task_statuses = {
            task.task_id: task.status for task in list_tasks(self.connection)
        }
        self.assertEqual(task_statuses[new_task_id], "done")

    def test_create_task_with_tags_preserves_task_creation(self):
        new_task_id = create_task_with_tags(
            self.connection,
            project_id=1,
            title="Add query summary report",
            priority=4,
            tag_ids=[1, 2],
        )

        task_ids = [task.task_id for task in list_tasks(self.connection)]
        self.assertIn(new_task_id, task_ids)

    def test_project_summary_returns_expected_rows(self):
        summaries = list_project_summaries(self.connection)
        self.assertEqual(len(summaries), 2)
        self.assertEqual(summaries[0].project_name, "AI Engineer Roadmap")


if __name__ == "__main__":
    unittest.main()

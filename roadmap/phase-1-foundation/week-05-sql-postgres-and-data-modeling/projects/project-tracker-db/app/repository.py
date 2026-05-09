"""
CRUD-style data access helpers for the Week 05 project tracker.
"""

from app.models import TaskRecord


def add_task(connection, project_id, title, priority, due_date=None):
    """Insert a new task and return its new database ID."""
    clean_title = title.strip()

    if not clean_title:
        raise ValueError("Task title cannot be empty.")

    with connection:
        cursor = connection.execute(
            """
            INSERT INTO tasks (project_id, title, status, priority, due_date)
            VALUES (?, ?, 'open', ?, ?)
            """,
            (project_id, clean_title, priority, due_date),
        )

    return cursor.lastrowid


def add_tag_to_task(connection, task_id, tag_id):
    """Connect one existing tag to one existing task."""
    with connection:
        connection.execute(
            "INSERT OR IGNORE INTO task_tags (task_id, tag_id) VALUES (?, ?)",
            (task_id, tag_id),
        )


def create_task_with_tags(connection, project_id, title, priority, tag_ids):
    """Create one task and connect all requested tags in one transaction."""
    with connection:
        cursor = connection.execute(
            """
            INSERT INTO tasks (project_id, title, status, priority)
            VALUES (?, ?, 'open', ?)
            """,
            (project_id, title.strip(), priority),
        )
        new_task_id = cursor.lastrowid

        for tag_id in tag_ids:
            connection.execute(
                "INSERT INTO task_tags (task_id, tag_id) VALUES (?, ?)",
                (new_task_id, tag_id),
            )

    return new_task_id


def list_tasks(connection):
    """Return all tasks with their project names."""
    rows = connection.execute(
        """
        SELECT
            tasks.id AS task_id,
            projects.name AS project_name,
            tasks.title,
            tasks.status,
            tasks.priority
        FROM tasks
        JOIN projects ON projects.id = tasks.project_id
        ORDER BY tasks.priority DESC, tasks.id ASC
        """
    ).fetchall()

    return [
        TaskRecord(
            task_id=row["task_id"],
            project_name=row["project_name"],
            title=row["title"],
            status=row["status"],
            priority=row["priority"],
        )
        for row in rows
    ]


def mark_task_done(connection, task_id):
    """Update one task so it is marked as done."""
    with connection:
        connection.execute(
            "UPDATE tasks SET status = 'done' WHERE id = ?",
            (task_id,),
        )


def delete_task(connection, task_id):
    """Delete one task and its tag relationships."""
    with connection:
        connection.execute("DELETE FROM task_tags WHERE task_id = ?", (task_id,))
        connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

"""
Report-style queries for the Week 05 project tracker.
"""

from app.models import ProjectSummary


def list_project_summaries(connection):
    """Return summary rows for each project with total and open task counts."""
    rows = connection.execute(
        """
        SELECT
            projects.id AS project_id,
            projects.name AS project_name,
            users.full_name AS owner_name,
            COUNT(tasks.id) AS total_tasks,
            SUM(CASE WHEN tasks.status = 'open' THEN 1 ELSE 0 END) AS open_tasks
        FROM projects
        JOIN users ON users.id = projects.owner_user_id
        LEFT JOIN tasks ON tasks.project_id = projects.id
        GROUP BY projects.id, projects.name, users.full_name
        ORDER BY projects.id
        """
    ).fetchall()

    return [
        ProjectSummary(
            project_id=row["project_id"],
            project_name=row["project_name"],
            owner_name=row["owner_name"],
            total_tasks=row["total_tasks"],
            open_tasks=row["open_tasks"] or 0,
        )
        for row in rows
    ]

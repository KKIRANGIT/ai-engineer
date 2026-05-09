"""
Small runnable demo for the Week 05 project tracker database project.
"""

from app.db import connect, initialize_database, seed_database
from app.reports import list_project_summaries
from app.repository import create_task_with_tags, list_tasks, mark_task_done


def reset_database(connection):
    """Start from a clean local database for the demo."""
    connection.executescript(
        """
        DROP TABLE IF EXISTS task_tags;
        DROP TABLE IF EXISTS tasks;
        DROP TABLE IF EXISTS tags;
        DROP TABLE IF EXISTS projects;
        DROP TABLE IF EXISTS users;
        """
    )
    initialize_database(connection)
    seed_database(connection)


def print_project_summaries(connection):
    """Print project summaries in a readable format."""
    print("\nProject summaries:")
    for summary in list_project_summaries(connection):
        print(
            f"- {summary.project_name} | "
            f"Owner: {summary.owner_name} | "
            f"Total tasks: {summary.total_tasks} | "
            f"Open tasks: {summary.open_tasks}"
        )


def print_tasks(connection):
    """Print all tasks in a readable format."""
    print("\nTasks:")
    for task in list_tasks(connection):
        print(
            f"- [{task.status}] {task.title} "
            f"(Project: {task.project_name}, Priority: {task.priority})"
        )


def main():
    """Run a small end-to-end database demo."""
    connection = connect()
    reset_database(connection)

    print_project_summaries(connection)
    print_tasks(connection)

    new_task_id = create_task_with_tags(
        connection,
        project_id=1,
        title="Review foreign key notes",
        priority=5,
        tag_ids=[2, 3],
    )
    mark_task_done(connection, new_task_id)

    print("-" * 40)
    print("After adding and completing one task:")
    print_project_summaries(connection)
    print_tasks(connection)

    connection.close()


if __name__ == "__main__":
    main()

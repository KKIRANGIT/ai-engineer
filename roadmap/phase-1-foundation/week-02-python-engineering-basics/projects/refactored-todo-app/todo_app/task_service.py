"""
Core task operations for the Week 02 todo app.

This module contains business logic that is easy to test.
"""

from todo_app.models import Task


def add_task(tasks: list[Task], title: str) -> Task:
    """Create a new task, append it to the list, and return it."""
    new_task = Task(title=title)
    tasks.append(new_task)
    return new_task


def validate_index(tasks: list[Task], task_index: int):
    """Raise an error if the requested task index is invalid."""
    if task_index < 0 or task_index >= len(tasks):
        raise IndexError("Task number is out of range.")


def mark_task_completed(tasks: list[Task], task_index: int):
    """Mark one task as completed using a zero-based index."""
    validate_index(tasks, task_index)
    tasks[task_index].mark_completed()


def delete_task(tasks: list[Task], task_index: int) -> Task:
    """Delete one task from the list and return the removed task."""
    validate_index(tasks, task_index)
    return tasks.pop(task_index)


def count_completed_tasks(tasks: list[Task]) -> int:
    """Count how many tasks are completed."""
    completed_total = 0

    for task in tasks:
        if task.completed:
            completed_total += 1

    return completed_total


def build_summary(tasks: list[Task]) -> str:
    """Return a human-readable summary of task progress."""
    total_tasks = len(tasks)
    completed_total = count_completed_tasks(tasks)
    pending_total = total_tasks - completed_total
    return (
        f"Total: {total_tasks}, "
        f"Completed: {completed_total}, "
        f"Pending: {pending_total}"
    )


def format_task(task: Task) -> str:
    """Return one task in a readable terminal-friendly format."""
    status = "Done" if task.completed else "Pending"
    return f"{task.title} [{status}]"

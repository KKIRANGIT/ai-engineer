import pytest

from todo_app.models import Task
from todo_app.task_service import (
    add_task,
    build_summary,
    count_completed_tasks,
    delete_task,
    mark_task_completed,
)


def test_add_task_appends_new_task():
    tasks = []
    created_task = add_task(tasks, "Study modules")

    assert created_task.title == "Study modules"
    assert len(tasks) == 1
    assert tasks[0].completed is False


def test_add_task_rejects_empty_title():
    tasks = []

    with pytest.raises(ValueError, match="Task title cannot be empty."):
        add_task(tasks, "   ")


def test_mark_task_completed_changes_state():
    tasks = [Task(title="Write tests")]
    mark_task_completed(tasks, 0)
    assert tasks[0].completed is True


def test_mark_task_completed_rejects_invalid_index():
    tasks = [Task(title="Write tests")]

    with pytest.raises(IndexError, match="Task number is out of range."):
        mark_task_completed(tasks, 3)


def test_delete_task_returns_removed_item():
    tasks = [Task(title="A"), Task(title="B")]
    removed_task = delete_task(tasks, 0)

    assert removed_task.title == "A"
    assert len(tasks) == 1
    assert tasks[0].title == "B"


def test_count_completed_tasks_counts_true_flags():
    tasks = [
        Task(title="A", completed=True),
        Task(title="B", completed=False),
        Task(title="C", completed=True),
    ]

    assert count_completed_tasks(tasks) == 2


def test_build_summary_reports_totals():
    tasks = [
        Task(title="A", completed=True),
        Task(title="B", completed=False),
    ]

    assert build_summary(tasks) == "Total: 2, Completed: 1, Pending: 1"

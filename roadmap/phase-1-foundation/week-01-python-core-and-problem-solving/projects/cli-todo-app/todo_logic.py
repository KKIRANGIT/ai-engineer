"""
Task operations for the CLI todo app.
"""


def create_task(task_title):
    """Build a new task dictionary."""
    return {
        "title": task_title,
        "completed": False,
    }


def add_task(tasks, task_title):
    """Add a new task to the task list."""
    clean_title = task_title.strip()

    if not clean_title:
        raise ValueError("Task title cannot be empty.")

    tasks.append(create_task(clean_title))


def list_tasks(tasks):
    """Print all tasks in a beginner-friendly numbered format."""
    if not tasks:
        print("\nNo tasks yet. Add your first task.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")


def mark_task_completed(tasks, task_index):
    """Mark one task as completed using a zero-based index."""
    validate_index(tasks, task_index)
    tasks[task_index]["completed"] = True


def delete_task(tasks, task_index):
    """Delete one task from the list using a zero-based index."""
    validate_index(tasks, task_index)
    tasks.pop(task_index)


def validate_index(tasks, task_index):
    """Raise an error if the provided task index is outside the valid range."""
    if task_index < 0 or task_index >= len(tasks):
        raise IndexError("Task number is out of range.")

"""
Storage helpers for the Week 02 todo app.

This module is responsible only for reading and writing task data.
"""

import json
from pathlib import Path

from todo_app.config import get_tasks_file
from todo_app.models import Task


def ensure_data_file_exists(file_path: Path | None = None) -> Path:
    """Create the parent folder and JSON file if they do not exist yet."""
    target_file = file_path or get_tasks_file()
    target_file.parent.mkdir(parents=True, exist_ok=True)

    if not target_file.exists():
        target_file.write_text("[]", encoding="utf-8")

    return target_file


def load_tasks(file_path: Path | None = None) -> list[Task]:
    """Load task records from JSON and convert them into Task objects."""
    target_file = ensure_data_file_exists(file_path)

    try:
        raw_text = target_file.read_text(encoding="utf-8").strip()

        if not raw_text:
            return []

        loaded_data = json.loads(raw_text)

        if not isinstance(loaded_data, list):
            raise ValueError("Task file must contain a list of task records.")

        return [Task.from_dict(item) for item in loaded_data]
    except json.JSONDecodeError as error:
        raise ValueError("Task file does not contain valid JSON.") from error


def save_tasks(tasks: list[Task], file_path: Path | None = None):
    """Convert Task objects into dictionaries and save them as JSON."""
    target_file = ensure_data_file_exists(file_path)
    task_data = [task.to_dict() for task in tasks]
    json_text = json.dumps(task_data, indent=2)
    target_file.write_text(json_text, encoding="utf-8")

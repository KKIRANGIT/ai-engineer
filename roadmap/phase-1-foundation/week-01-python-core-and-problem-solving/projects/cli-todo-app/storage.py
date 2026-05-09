"""
Storage helpers for the CLI todo app.

This file is responsible for only one concern:
loading task data from disk and saving task data back to disk.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "tasks.json"


def ensure_data_file_exists():
    """Create the data folder and file if they do not exist yet."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def is_valid_task(task):
    """Return True only if a task uses the expected dictionary shape."""
    return (
        isinstance(task, dict)
        and isinstance(task.get("title"), str)
        and isinstance(task.get("completed"), bool)
    )


def normalize_tasks(raw_tasks):
    """Keep only valid task dictionaries and discard broken entries."""
    clean_tasks = []

    for task in raw_tasks:
        if is_valid_task(task):
            clean_tasks.append(task)

    return clean_tasks


def load_tasks():
    """Load tasks from JSON and recover safely from missing or broken data."""
    ensure_data_file_exists()

    try:
        file_text = DATA_FILE.read_text(encoding="utf-8").strip()

        if not file_text:
            return []

        loaded_data = json.loads(file_text)

        # We expect a list because each task is one item in an ordered collection.
        if not isinstance(loaded_data, list):
            print("Warning: task file should contain a list. Starting with an empty list.")
            return []

        return normalize_tasks(loaded_data)
    except json.JSONDecodeError:
        print("Warning: task file was not valid JSON. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the current task list back to the JSON file."""
    ensure_data_file_exists()

    # indent=2 makes the JSON easier for a beginner to open and inspect manually.
    json_text = json.dumps(tasks, indent=2)
    DATA_FILE.write_text(json_text, encoding="utf-8")

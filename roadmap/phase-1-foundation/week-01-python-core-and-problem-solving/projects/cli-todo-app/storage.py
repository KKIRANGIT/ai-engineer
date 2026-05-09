"""
Storage helpers for the CLI todo app.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "tasks.json"


def ensure_data_file_exists():
    """Create the data folder and file if they do not exist yet."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")


def load_tasks():
    """Load tasks from the JSON file and return an empty list if needed."""
    ensure_data_file_exists()

    try:
        file_text = DATA_FILE.read_text(encoding="utf-8").strip()
        if not file_text:
            return []
        return json.loads(file_text)
    except json.JSONDecodeError:
        print("Warning: task file was not valid JSON. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save the current task list back to the JSON file."""
    ensure_data_file_exists()
    json_text = json.dumps(tasks, indent=2)
    DATA_FILE.write_text(json_text, encoding="utf-8")

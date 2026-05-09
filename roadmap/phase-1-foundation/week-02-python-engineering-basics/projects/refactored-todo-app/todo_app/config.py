"""
Configuration helpers for the Week 02 todo app.

This module keeps environment-aware settings separate from the core logic.
"""

import os
from pathlib import Path

DEFAULT_TASKS_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"
TASKS_FILE_ENV_NAME = "TODO_TASKS_FILE"


def get_tasks_file() -> Path:
    """Return the task storage file path, using an env override when available."""
    override_value = os.getenv(TASKS_FILE_ENV_NAME)

    if not override_value:
        return DEFAULT_TASKS_FILE

    override_path = Path(override_value).expanduser()

    # Relative paths are resolved from the current working directory.
    if not override_path.is_absolute():
        override_path = Path.cwd() / override_path

    return override_path

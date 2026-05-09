"""
Data model definitions for the Week 02 todo app.

This file introduces one small dataclass so task shape becomes explicit.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represent one todo item in a structured, readable way."""

    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate task data after the dataclass is created."""
        clean_title = self.title.strip()

        if not clean_title:
            raise ValueError("Task title cannot be empty.")

        self.title = clean_title

    def mark_completed(self):
        """Update the task so it is marked as completed."""
        self.completed = True

    def to_dict(self) -> dict[str, str | bool]:
        """Convert the task object into plain dictionary data for JSON storage."""
        return {
            "title": self.title,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, raw_data: dict) -> "Task":
        """Create a Task object from a dictionary after validating its shape."""
        if not isinstance(raw_data, dict):
            raise ValueError("Each stored task must be a dictionary.")

        title = raw_data.get("title")
        completed = raw_data.get("completed", False)

        if not isinstance(title, str):
            raise ValueError("Task title must be a string.")

        if not isinstance(completed, bool):
            raise ValueError("Task completed flag must be a boolean.")

        return cls(title=title, completed=completed)

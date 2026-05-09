"""
Week 02 - Classes: A Small Dataclass Example

What this file teaches:
- how a dataclass can make data shape explicit
- how one object can also contain small helper behavior
- how to convert an object into a dictionary form
"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represent one task with a title and completion state."""

    title: str
    completed: bool = False

    def mark_completed(self):
        """Update this task object to completed."""
        self.completed = True

    def to_dict(self):
        """Convert the task into a plain dictionary for storage or JSON."""
        return {
            "title": self.title,
            "completed": self.completed,
        }


def show_example():
    """Demonstrate how a task object changes over time."""
    task = Task(title="Refactor the todo app")
    print("Before completion:", task)
    task.mark_completed()
    print("After completion:", task)
    print("As dictionary:", task.to_dict())


if __name__ == "__main__":
    show_example()

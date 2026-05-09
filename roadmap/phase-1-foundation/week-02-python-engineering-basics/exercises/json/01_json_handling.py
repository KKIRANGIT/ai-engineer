"""
Week 02 - JSON: Structured Data In and Out

What this file teaches:
- how Python data becomes JSON text
- how JSON text becomes Python data again
- why validating the loaded shape matters
"""

import json


def build_task_records():
    """Return a small list of task dictionaries."""
    return [
        {"title": "Study modules", "completed": False},
        {"title": "Practice pytest", "completed": True},
    ]


def to_json_text(task_records):
    """Convert Python data into formatted JSON text."""
    return json.dumps(task_records, indent=2)


def from_json_text(json_text):
    """Parse JSON text back into Python data."""
    loaded_data = json.loads(json_text)

    if not isinstance(loaded_data, list):
        raise ValueError("Expected a list of task records.")

    return loaded_data


def show_example():
    """Demonstrate the round-trip between Python data and JSON text."""
    task_records = build_task_records()
    json_text = to_json_text(task_records)

    print("JSON text:")
    print(json_text)

    loaded_tasks = from_json_text(json_text)
    print("Loaded Python data:", loaded_tasks)


if __name__ == "__main__":
    show_example()

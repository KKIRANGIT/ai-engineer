import json

import pytest

from todo_app.models import Task
from todo_app.storage import load_tasks, save_tasks


def test_save_tasks_writes_json_file(tmp_path):
    file_path = tmp_path / "tasks.json"
    tasks = [Task(title="Study JSON"), Task(title="Write tests", completed=True)]

    save_tasks(tasks, file_path)

    stored_data = json.loads(file_path.read_text(encoding="utf-8"))
    assert stored_data == [
        {"title": "Study JSON", "completed": False},
        {"title": "Write tests", "completed": True},
    ]


def test_load_tasks_returns_task_objects(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text(
        json.dumps([{"title": "Read docs", "completed": True}]),
        encoding="utf-8",
    )

    tasks = load_tasks(file_path)

    assert len(tasks) == 1
    assert tasks[0].title == "Read docs"
    assert tasks[0].completed is True


def test_load_tasks_rejects_invalid_json(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text("{broken json", encoding="utf-8")

    with pytest.raises(ValueError, match="Task file does not contain valid JSON."):
        load_tasks(file_path)


def test_load_tasks_rejects_wrong_top_level_shape(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text(json.dumps({"title": "wrong shape"}), encoding="utf-8")

    with pytest.raises(ValueError, match="Task file must contain a list of task records."):
        load_tasks(file_path)

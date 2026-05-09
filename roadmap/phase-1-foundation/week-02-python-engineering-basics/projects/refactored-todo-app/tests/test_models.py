from todo_app.models import Task


def test_task_trims_title():
    task = Task(title="  Study pytest  ")
    assert task.title == "Study pytest"


def test_task_rejects_empty_title():
    try:
        Task(title="   ")
        assert False, "Expected ValueError for empty task title."
    except ValueError as error:
        assert str(error) == "Task title cannot be empty."


def test_task_to_dict():
    task = Task(title="Refactor app", completed=True)
    assert task.to_dict() == {"title": "Refactor app", "completed": True}


def test_task_from_dict_builds_task():
    task = Task.from_dict({"title": "Write tests", "completed": False})
    assert task.title == "Write tests"
    assert task.completed is False

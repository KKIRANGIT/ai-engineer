# Refactored Todo App

This project is the Week 02 upgrade of the Week 01 todo app.

## What This Project Teaches

- package-style structure
- module boundaries
- type hints
- dataclass-based data modeling
- safer JSON loading and saving
- validation through raised exceptions
- basic automated testing with `pytest`

## Project Structure

```text
refactored-todo-app/
|-- todo_app/
|   |-- __init__.py
|   |-- app.py
|   |-- config.py
|   |-- models.py
|   |-- storage.py
|   `-- task_service.py
|-- tests/
|   |-- test_models.py
|   |-- test_storage.py
|   `-- test_task_service.py
|-- data/
|   `-- tasks.json
|-- .env.example
`-- README.md
```

## How To Run

From this folder:

```powershell
python -m todo_app.app
```

## How To Run Tests

If `pytest` is installed:

```powershell
pytest
```

If `pytest` is not installed yet:

```powershell
python -m pip install pytest
```

## Environment Variable Pattern

This project supports an optional environment variable:

- `TODO_TASKS_FILE`

If provided, the app will use that file path for task storage instead of the default `data/tasks.json`.

See [.env.example](./.env.example) for the example format.

## Engineering Lessons In This Version

- the CLI lives in `app.py`
- the data model lives in `models.py`
- the core task operations live in `task_service.py`
- file persistence lives in `storage.py`
- environment-aware path configuration lives in `config.py`
- tests focus mostly on pure logic and controlled storage behavior

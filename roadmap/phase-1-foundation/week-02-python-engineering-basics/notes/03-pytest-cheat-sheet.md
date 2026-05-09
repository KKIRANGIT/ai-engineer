# Pytest Cheat Sheet

## Basic run command

```powershell
pytest
```

## Run a specific file

```powershell
pytest tests/test_task_service.py
```

## Common patterns

### Simple assertion

```python
def test_addition():
    assert 2 + 2 == 4
```

### Expected exception

```python
import pytest

def test_invalid_input():
    with pytest.raises(ValueError):
        int("abc")
```

### Temporary path fixture

`tmp_path` gives you a safe temporary folder for file-based tests.

```python
def test_write_file(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("hello", encoding="utf-8")
    assert file_path.read_text(encoding="utf-8") == "hello"
```

## Testing mindset

- test one behavior at a time
- include failure cases, not only success cases
- keep tests readable
- treat tests as executable explanations of expected behavior

"""
Week 02 - Type Hints: Clearer Function Contracts

What this file teaches:
- how type hints describe expected inputs and outputs
- how type hints help readability without changing runtime behavior
"""

from pathlib import Path


def build_task_file_path(base_folder: Path, file_name: str) -> Path:
    """Return the full path for a task data file."""
    return base_folder / file_name


def count_completed_flags(completion_flags: list[bool]) -> int:
    """Count how many items in the list are True."""
    completed_total = 0

    for flag in completion_flags:
        if flag:
            completed_total += 1

    return completed_total


def summarize_scores(scores: dict[str, int]) -> str:
    """Return a short summary string for a score dictionary."""
    student_count = len(scores)
    total_score = sum(scores.values())
    return f"Students: {student_count}, Total Score: {total_score}"


def show_example():
    """Run small examples that use typed helper functions."""
    data_path = build_task_file_path(Path("data"), "tasks.json")
    print("Data path:", data_path)
    print("Completed total:", count_completed_flags([True, False, True, True]))
    print("Score summary:", summarize_scores({"Asha": 8, "Ravi": 6}))


if __name__ == "__main__":
    show_example()

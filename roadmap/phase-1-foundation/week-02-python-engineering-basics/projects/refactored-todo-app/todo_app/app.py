"""
Main CLI entry point for the Week 02 refactored todo app.

This file handles:
- menu display
- user input
- calling the correct service functions
- saving changes after mutations
"""

from todo_app.storage import load_tasks, save_tasks
from todo_app.task_service import (
    add_task,
    build_summary,
    delete_task,
    format_task,
    mark_task_completed,
)


def show_menu():
    """Display the available actions."""
    print("\n--- Refactored Todo App ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Show summary")
    print("6. Exit")


def list_tasks(tasks):
    """Print all current tasks in a readable numbered format."""
    if not tasks:
        print("\nNo tasks yet. Add your first task.")
        return

    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {format_task(task)}")


def get_task_number(prompt_text: str) -> int:
    """Read a whole-number task selection from the user."""
    raw_input_value = input(prompt_text).strip()

    if not raw_input_value.isdigit():
        raise ValueError("Please enter a valid whole number.")

    return int(raw_input_value)


def handle_add_task(tasks):
    """Add a task and save the updated list."""
    title = input("Enter the new task title: ")
    add_task(tasks, title)
    save_tasks(tasks)
    print("Task added successfully.")


def handle_mark_completed(tasks):
    """Mark a chosen task as complete and save the change."""
    list_tasks(tasks)
    task_number = get_task_number("Enter the task number to mark complete: ")
    mark_task_completed(tasks, task_number - 1)
    save_tasks(tasks)
    print("Task marked as complete.")


def handle_delete_task(tasks):
    """Delete a chosen task and save the change."""
    list_tasks(tasks)
    task_number = get_task_number("Enter the task number to delete: ")
    removed_task = delete_task(tasks, task_number - 1)
    save_tasks(tasks)
    print(f"Deleted task: {removed_task.title}")


def main():
    """Run the main application loop until the user exits."""
    try:
        tasks = load_tasks()
    except ValueError as error:
        print(f"Error loading tasks: {error}")
        tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            list_tasks(tasks)

        elif choice == "2":
            try:
                handle_add_task(tasks)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            try:
                handle_mark_completed(tasks)
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif choice == "4":
            try:
                handle_delete_task(tasks)
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif choice == "5":
            print(build_summary(tasks))

        elif choice == "6":
            print("Goodbye. Your Week 02 project is ready for further upgrades.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

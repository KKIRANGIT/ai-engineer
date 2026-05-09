"""
Main user interface for the CLI todo app.

This file handles:
- showing the menu
- reading user input
- calling the correct task logic
- saving changes after task updates
"""

from storage import load_tasks, save_tasks
from todo_logic import add_task, delete_task, list_tasks, mark_task_completed


def show_menu():
    """Display the available actions."""
    print("\n--- CLI Todo App ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")


def get_task_number(prompt_text):
    """Ask the user for a task number and return it as an integer."""
    user_input = input(prompt_text).strip()

    if not user_input.isdigit():
        raise ValueError("Please enter a valid whole number.")

    return int(user_input)


def handle_add_task(tasks):
    """Create a new task, then save the updated task list."""
    task_title = input("Enter the new task title: ")
    add_task(tasks, task_title)
    save_tasks(tasks)
    print("Task added successfully.")


def handle_mark_complete(tasks):
    """Mark one task as completed, then save the updated task list."""
    list_tasks(tasks)
    task_number = get_task_number("Enter the task number to mark complete: ")

    # Subtract 1 because users count from 1, but Python lists count from 0.
    mark_task_completed(tasks, task_number - 1)
    save_tasks(tasks)
    print("Task marked as complete.")


def handle_delete_task(tasks):
    """Delete one task, then save the updated task list."""
    list_tasks(tasks)
    task_number = get_task_number("Enter the task number to delete: ")
    delete_task(tasks, task_number - 1)
    save_tasks(tasks)
    print("Task deleted.")


def main():
    """Run the todo application loop until the user exits."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)

        elif choice == "2":
            try:
                handle_add_task(tasks)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            try:
                handle_mark_complete(tasks)
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif choice == "4":
            try:
                handle_delete_task(tasks)
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif choice == "5":
            print("Goodbye. Keep shipping small projects.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()

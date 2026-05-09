"""
Main user interface for the CLI todo app.
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
    """Ask the user for a task number."""
    user_input = input(prompt_text).strip()

    if not user_input.isdigit():
        raise ValueError("Please enter a valid whole number.")

    return int(user_input)


def main():
    """Run the todo application loop."""
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)

        elif choice == "2":
            task_title = input("Enter the new task title: ")

            try:
                add_task(tasks, task_title)
                save_tasks(tasks)
                print("Task added successfully.")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "3":
            list_tasks(tasks)

            try:
                task_number = get_task_number("Enter the task number to mark complete: ")
                mark_task_completed(tasks, task_number - 1)
                save_tasks(tasks)
                print("Task marked as complete.")
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif choice == "4":
            list_tasks(tasks)

            try:
                task_number = get_task_number("Enter the task number to delete: ")
                delete_task(tasks, task_number - 1)
                save_tasks(tasks)
                print("Task deleted.")
            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif choice == "5":
            print("Goodbye. Keep shipping small projects.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()

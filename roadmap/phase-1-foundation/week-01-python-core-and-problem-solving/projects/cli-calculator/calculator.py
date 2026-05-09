"""
Simple CLI calculator for Week 01.

The goal of this file is not to be the shortest calculator possible.
The goal is to be readable and beginner-friendly.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the division result and reject division by zero."""
    if second_number == 0:
        raise ValueError("You cannot divide by zero.")

    return first_number / second_number


def show_menu():
    """Display the list of actions the user can choose from."""
    print("\n--- CLI Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def get_number(prompt_text):
    """Ask the user for a number until a valid number is entered."""
    while True:
        user_input = input(prompt_text).strip()

        try:
            return float(user_input)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def perform_calculation(choice, first_number, second_number):
    """Pick the correct operation based on the user's menu choice."""
    if choice == "1":
        return add(first_number, second_number)
    if choice == "2":
        return subtract(first_number, second_number)
    if choice == "3":
        return multiply(first_number, second_number)
    if choice == "4":
        return divide(first_number, second_number)

    raise ValueError("Unknown menu choice.")


def main():
    """Run the main calculator loop."""
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye. Keep practicing Python.")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid menu choice. Please select a number from 1 to 5.")
            continue

        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        try:
            result = perform_calculation(choice, first_number, second_number)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()

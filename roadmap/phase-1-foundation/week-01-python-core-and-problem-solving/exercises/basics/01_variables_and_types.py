"""
Week 01 - Basics: Variables and Types

What this file teaches:
- how variables store values
- how different Python types behave
- how one variable name can later point to a different type
- how arithmetic and string formatting work
"""


def show_basic_values():
    """Print a few variables with different built-in Python types."""
    student_name = "Asha"
    age = 24
    height_in_meters = 1.68
    is_learning_python = True

    print("Student name:", student_name)
    print("Age:", age)
    print("Height:", height_in_meters)
    print("Is learning Python:", is_learning_python)

    # type(...) lets you inspect what kind of value a variable currently holds.
    print("Type of student_name:", type(student_name))
    print("Type of age:", type(age))
    print("Type of height_in_meters:", type(height_in_meters))
    print("Type of is_learning_python:", type(is_learning_python))


def show_dynamic_typing():
    """Demonstrate that one variable name can point to different value types."""
    value = 10
    print("Value before change:", value, type(value))

    # Python is dynamically typed, so the same name can later point to a string.
    value = "ten"
    print("Value after change:", value, type(value))


def show_numeric_operations():
    """Demonstrate common arithmetic operators."""
    first_number = 12
    second_number = 5

    print("Addition:", first_number + second_number)
    print("Subtraction:", first_number - second_number)
    print("Multiplication:", first_number * second_number)
    print("Division:", first_number / second_number)
    print("Floor division:", first_number // second_number)
    print("Remainder:", first_number % second_number)


def show_string_building():
    """Show two common ways to build strings."""
    greeting = "Hello"
    target = "Python"
    message = greeting + ", " + target
    print("Combined string:", message)

    student_name = "Asha"
    age = 24

    # f-strings are usually the cleanest way to insert values into text.
    formatted_message = f"{student_name} is {age} years old."
    print("Formatted string:", formatted_message)


def show_none_value():
    """Explain how None represents the absence of a real value."""
    middle_name = None
    print("Middle name:", middle_name)
    print("Type of middle_name:", type(middle_name))


def show_small_price_example():
    """Use variables in a small real-life calculation."""
    price = 99.99
    discount = 10
    final_price = price - discount
    print(f"Final price after discount: {final_price}")


def main():
    """Run all examples in a clear top-to-bottom order."""
    show_basic_values()
    print("-" * 40)
    show_dynamic_typing()
    print("-" * 40)
    show_numeric_operations()
    print("-" * 40)
    show_string_building()
    print("-" * 40)
    show_none_value()
    print("-" * 40)
    show_small_price_example()


if __name__ == "__main__":
    main()

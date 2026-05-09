"""
Week 01 - Functions: Small Reusable Blocks of Logic

What this file teaches:
- how to define functions
- how parameters bring data into a function
- how return values send results back out
- how one function can reuse another function
"""


def greet_user(name):
    """Return a friendly greeting message."""
    return f"Hello, {name}!"


def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def is_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


def count_words(sentence):
    """Return how many words appear in a sentence."""
    words = sentence.split()
    return len(words)


def describe_number(number):
    """Return a sentence describing whether a number is odd or even."""
    # Reusing is_even(...) keeps this function simple and readable.
    if is_even(number):
        kind = "even"
    else:
        kind = "odd"

    return f"The number {number} is {kind}."


def calculate_rectangle_area(length, width):
    """Return the rectangle area."""
    return length * width


def main():
    """Call each function so you can see inputs and outputs clearly."""
    print(greet_user("Asha"))
    print("10 + 5 =", add_numbers(10, 5))
    print("Is 8 even?", is_even(8))
    print("Word count:", count_words("Python makes problem solving easier"))
    print(describe_number(7))
    print(describe_number(14))
    print("Rectangle area:", calculate_rectangle_area(4, 6))


if __name__ == "__main__":
    main()

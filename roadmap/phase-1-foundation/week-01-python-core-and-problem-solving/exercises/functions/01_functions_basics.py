"""
Week 01 - Functions: Small Reusable Blocks of Logic
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


print(greet_user("Asha"))
print("10 + 5 =", add_numbers(10, 5))
print("Is 8 even?", is_even(8))
print("Word count:", count_words("Python makes problem solving easier"))


def describe_number(number):
    """Return a sentence describing whether a number is odd or even."""
    if is_even(number):
        kind = "even"
    else:
        kind = "odd"

    return f"The number {number} is {kind}."


print(describe_number(7))
print(describe_number(14))


def calculate_rectangle_area(length, width):
    """Return the rectangle area."""
    return length * width


print("Rectangle area:", calculate_rectangle_area(4, 6))

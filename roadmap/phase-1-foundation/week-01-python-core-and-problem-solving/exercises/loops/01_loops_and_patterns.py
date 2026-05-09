"""
Week 01 - Loops: Repeating Work Cleanly

What this file teaches:
- basic for loops with range
- using a loop to accumulate a result
- while loops for repeated actions based on a condition
- break and continue
- small loop-based problem solving
"""


def show_for_loop_with_range():
    """Loop through a fixed range of numbers."""
    for number in range(1, 6):
        print("Number:", number)


def show_accumulation_pattern():
    """Use a loop to build up a running total."""
    even_total = 0

    for number in range(1, 11):
        if number % 2 == 0:
            even_total += number

    print("Sum of even numbers from 1 to 10:", even_total)


def show_while_loop():
    """Repeat work until a condition becomes false."""
    count = 3

    while count > 0:
        print("Countdown:", count)
        count -= 1

    print("Blast off!")


def show_break_example():
    """Stop a loop as soon as the needed value is found."""
    numbers = [4, 7, 9, 12, 15]

    for number in numbers:
        if number % 2 == 0:
            print("First even number found:", number)
            break


def show_continue_example():
    """Skip one loop iteration and keep going."""
    for number in range(1, 6):
        if number == 3:
            continue

        print("Number except 3:", number)


def build_stars(rows):
    """Return a list of star-pattern lines."""
    pattern_lines = []

    for row in range(1, rows + 1):
        pattern_lines.append("*" * row)

    return pattern_lines


def find_maximum(values):
    """Find the largest value manually without using max()."""
    largest = values[0]

    for value in values:
        if value > largest:
            largest = value

    return largest


def show_problem_solving_examples():
    """Use loops to build patterns and inspect values."""
    for line in build_stars(5):
        print(line)

    sample_values = [14, 7, 22, 19, 5]
    print("Largest value:", find_maximum(sample_values))


def main():
    """Run all loop examples in learning order."""
    show_for_loop_with_range()
    print("-" * 40)
    show_accumulation_pattern()
    print("-" * 40)
    show_while_loop()
    print("-" * 40)
    show_break_example()
    show_continue_example()
    print("-" * 40)
    show_problem_solving_examples()


if __name__ == "__main__":
    main()

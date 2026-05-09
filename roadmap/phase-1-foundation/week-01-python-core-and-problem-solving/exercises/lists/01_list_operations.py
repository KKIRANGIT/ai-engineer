"""
Week 01 - Lists: Ordered and Mutable Collections

What this file teaches:
- how to add, insert, and remove list items
- how indexing and slicing work
- how to loop through a list
- how to solve a small list problem with a helper function
"""


def show_basic_list_updates():
    """Demonstrate common list operations that change the list in place."""
    tasks = ["study Python", "walk", "read docs"]
    print("Original tasks:", tasks)

    tasks.append("practice coding")
    print("After append:", tasks)

    tasks.insert(1, "drink water")
    print("After insert:", tasks)

    tasks.remove("walk")
    print("After remove:", tasks)

    removed_task = tasks.pop(0)
    print("Removed task:", removed_task)
    print("After pop:", tasks)

    return tasks


def show_indexing_and_slicing(tasks):
    """Read specific items from the updated task list."""
    print("First task:", tasks[0])
    print("Last task:", tasks[-1])
    print("First two tasks:", tasks[:2])


def show_loops(tasks):
    """Print the list with and without numbering."""
    for task in tasks:
        print("Task:", task)

    # enumerate gives both the position and the value at the same time.
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def remove_duplicates(values):
    """Return a new list with duplicates removed while keeping first-seen order."""
    unique_values = []

    for value in values:
        # We only append values that have not been seen before.
        if value not in unique_values:
            unique_values.append(value)

    return unique_values


def show_problem_solving_examples():
    """Run a few examples that feel closer to real list usage."""
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Without duplicates:", remove_duplicates(numbers))

    # This list comprehension is short and readable, so it is a good fit here.
    squares = [number * number for number in range(1, 6)]
    print("Squares:", squares)


def main():
    """Run all list examples in a clean order."""
    tasks = show_basic_list_updates()
    print("-" * 40)
    show_indexing_and_slicing(tasks)
    print("-" * 40)
    show_loops(tasks)
    print("-" * 40)
    show_problem_solving_examples()


if __name__ == "__main__":
    main()

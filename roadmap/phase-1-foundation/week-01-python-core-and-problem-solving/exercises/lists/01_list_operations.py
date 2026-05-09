"""
Week 01 - Lists: Ordered and Mutable Collections
"""

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

print("First task:", tasks[0])
print("Last task:", tasks[-1])
print("First two tasks:", tasks[:2])

for task in tasks:
    print("Task:", task)

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")


def remove_duplicates(values):
    """Return a new list with duplicates removed while keeping the first appearance order."""
    unique_values = []

    for value in values:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values


numbers = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", remove_duplicates(numbers))

squares = [number * number for number in range(1, 6)]
print("Squares:", squares)

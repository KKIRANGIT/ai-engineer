"""
Week 01 - Basics: Variables and Types

This file is designed for a complete beginner.
Read the comments slowly and run the file after every small change.
"""

student_name = "Asha"
age = 24
height_in_meters = 1.68
is_learning_python = True

print("Student name:", student_name)
print("Age:", age)
print("Height:", height_in_meters)
print("Is learning Python:", is_learning_python)

print(type(student_name))
print(type(age))
print(type(height_in_meters))
print(type(is_learning_python))

value = 10
print("Value before change:", value, type(value))

value = "ten"
print("Value after change:", value, type(value))

first_number = 12
second_number = 5

print("Addition:", first_number + second_number)
print("Subtraction:", first_number - second_number)
print("Multiplication:", first_number * second_number)
print("Division:", first_number / second_number)
print("Floor division:", first_number // second_number)
print("Remainder:", first_number % second_number)

greeting = "Hello"
target = "Python"
message = greeting + ", " + target
print(message)

formatted_message = f"{student_name} is {age} years old."
print(formatted_message)

middle_name = None
print("Middle name:", middle_name)
print("Type of middle_name:", type(middle_name))

price = 99.99
discount = 10
final_price = price - discount
print(f"Final price after discount: {final_price}")

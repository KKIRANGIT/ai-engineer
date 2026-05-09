"""
Week 01 - Basics: Truthiness and Conditionals

This file shows how Python decides whether a condition is true or false.
"""

print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('hello'):", bool("hello"))
print("bool(''):", bool(""))
print("bool([1, 2, 3]):", bool([1, 2, 3]))
print("bool([]):", bool([]))
print("bool({'name': 'Asha'}):", bool({"name": "Asha"}))
print("bool({}):", bool({}))
print("bool(None):", bool(None))

temperature = 32
if temperature > 30:
    print("It is hot today.")

score = 78

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")

fruit = "apple"
favorite_fruits = ["apple", "banana", "mango"]

if fruit in favorite_fruits:
    print(f"{fruit} is in the favorite list.")

first_name = "Asha"
second_name = "Asha"
print("Value comparison with ==:", first_name == second_name)

user_email = None
if user_email is None:
    print("Email is missing.")

shopping_cart = []
if shopping_cart:
    print("The cart has items.")
else:
    print("The cart is empty.")

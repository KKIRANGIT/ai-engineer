"""
Week 01 - Basics: Truthiness and Conditionals

What this file teaches:
- how Python converts values to True or False
- how if/elif/else blocks choose a code path
- why `==` and `is` mean different things
"""


def show_truthiness_examples():
    """Display values that Python treats as truthy or falsey."""
    print("bool(1):", bool(1))
    print("bool(0):", bool(0))
    print("bool('hello'):", bool("hello"))
    print("bool(''):", bool(""))
    print("bool([1, 2, 3]):", bool([1, 2, 3]))
    print("bool([]):", bool([]))
    print("bool({'name': 'Asha'}):", bool({"name": "Asha"}))
    print("bool({}):", bool({}))
    print("bool(None):", bool(None))


def show_simple_if_statement():
    """Use a single condition to decide whether to print a message."""
    temperature = 32

    if temperature > 30:
        print("It is hot today.")


def show_if_elif_else_chain():
    """Choose one branch from multiple grade ranges."""
    score = 78

    if score >= 90:
        print("Grade: A")
    elif score >= 75:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: D")


def show_membership_check():
    """Check whether one value appears inside a collection."""
    fruit = "apple"
    favorite_fruits = ["apple", "banana", "mango"]

    if fruit in favorite_fruits:
        print(f"{fruit} is in the favorite list.")


def show_value_comparison():
    """Use == when comparing values."""
    first_name = "Asha"
    second_name = "Asha"
    print("Value comparison with ==:", first_name == second_name)


def show_identity_check():
    """Use `is None` when checking whether a value is missing."""
    user_email = None

    if user_email is None:
        print("Email is missing.")


def show_falsey_collection():
    """Empty collections become False in conditions."""
    shopping_cart = []

    if shopping_cart:
        print("The cart has items.")
    else:
        print("The cart is empty.")


def main():
    """Run all truthiness and condition examples."""
    show_truthiness_examples()
    print("-" * 40)
    show_simple_if_statement()
    show_if_elif_else_chain()
    show_membership_check()
    show_value_comparison()
    show_identity_check()
    show_falsey_collection()


if __name__ == "__main__":
    main()

"""
Week 02 - Validation: Exceptions and Safe Boundaries

What this file teaches:
- how to reject invalid input early
- when to raise ValueError
- why clear validation messages are useful
"""


def parse_age(user_input):
    """Convert a raw age string into a validated integer age."""
    clean_input = user_input.strip()

    if not clean_input:
        raise ValueError("Age cannot be empty.")

    age = int(clean_input)

    if age < 0:
        raise ValueError("Age cannot be negative.")

    return age


def categorize_age(age):
    """Return a simple age category string."""
    if age < 13:
        return "child"
    if age < 20:
        return "teen"
    if age < 60:
        return "adult"
    return "senior"


def show_example():
    """Demonstrate successful validation and conversion."""
    raw_value = " 24 "
    age = parse_age(raw_value)
    print(f"Validated age: {age}")
    print(f"Category: {categorize_age(age)}")


if __name__ == "__main__":
    show_example()

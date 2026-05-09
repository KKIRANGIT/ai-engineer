"""
Week 02 - Modules: Separating Responsibilities

What this file teaches:
- how one program can be described in layers
- why separating responsibilities makes code easier to test and maintain
- how helper functions can model different parts of an application
"""


def collect_user_request(raw_name, raw_quantity):
    """Simulate collecting raw data from a user or another outside source."""
    return {
        "name": raw_name,
        "quantity": raw_quantity,
    }


def validate_request(request_data):
    """Validate that incoming request data has the shape we expect."""
    name = request_data["name"].strip()

    if not name:
        raise ValueError("Item name cannot be empty.")

    quantity = int(request_data["quantity"])

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return {
        "name": name,
        "quantity": quantity,
    }


def build_summary(valid_request):
    """Create the core result without printing or asking for input."""
    return f"Added {valid_request['quantity']} unit(s) of {valid_request['name']}."


def show_example():
    """Run the example from raw input to validated result."""
    raw_request = collect_user_request(" notebook ", "3")
    valid_request = validate_request(raw_request)
    summary = build_summary(valid_request)
    print(summary)


if __name__ == "__main__":
    show_example()

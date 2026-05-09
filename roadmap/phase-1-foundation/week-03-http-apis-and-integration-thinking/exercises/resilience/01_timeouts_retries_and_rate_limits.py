"""
Week 03 - Resilience: Timeout and Retry Thinking

What this file teaches:
- that not every failure should be retried
- how a simple backoff pattern can be represented
- why 429 and 5xx responses deserve special attention
"""


def should_retry(status_code):
    """Return True for status codes that are often worth retrying."""
    return status_code == 429 or 500 <= status_code <= 599


def calculate_backoff_seconds(attempt_number):
    """Return a simple linear backoff delay."""
    return attempt_number * 2


def show_example():
    """Demonstrate retry decisions for several status codes."""
    sample_status_codes = [200, 404, 429, 500, 503]

    for status_code in sample_status_codes:
        print(
            f"Status {status_code} -> retry: {should_retry(status_code)}"
        )

    print("-" * 40)
    for attempt_number in range(1, 4):
        print(
            f"Attempt {attempt_number} backoff: "
            f"{calculate_backoff_seconds(attempt_number)} seconds"
        )


if __name__ == "__main__":
    show_example()

"""
This exercise demonstrates why semantic similarity alone can still return
wrong-scope content when metadata filters are not applied.
"""


def main():
    results_without_filter = [
        {"title": "Refund Policy", "audience": "customers", "score": 0.93},
        {"title": "Internal Billing Escalation Guide", "audience": "staff", "score": 0.91},
        {"title": "Subscription Cancellation FAQ", "audience": "customers", "score": 0.88},
    ]

    filtered_results = [item for item in results_without_filter if item["audience"] == "customers"]

    print("Results without audience filter:")
    for item in results_without_filter:
        print(item)

    print("\nResults after filtering to customer-facing content:")
    for item in filtered_results:
        print(item)


if __name__ == "__main__":
    main()

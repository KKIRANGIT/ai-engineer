"""Show why retry counters belong in workflow state."""

from __future__ import annotations


def retrieve_with_retry(found_docs: int) -> None:
    retry_count = 0

    while found_docs == 0 and retry_count < 2:
        print(f"No docs found. Retrying with retry_count={retry_count + 1}")
        retry_count += 1
        found_docs = 1

    print(f"Final found_docs={found_docs}, retry_count={retry_count}")


if __name__ == "__main__":
    retrieve_with_retry(found_docs=0)

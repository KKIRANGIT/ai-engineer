"""
Week 06 - Concurrency: Gathering multiple I/O-style tasks
"""

import asyncio


async def load_source(source_name, delay_seconds):
    """Simulate loading one external source."""
    await asyncio.sleep(delay_seconds)
    return {
        "source_name": source_name,
        "record_count": delay_seconds * 10,
    }


async def main():
    """Load several simulated sources concurrently."""
    source_tasks = [
        load_source("events", 1),
        load_source("metadata", 2),
        load_source("scores", 1),
    ]

    results = await asyncio.gather(*source_tasks)

    print("Loaded sources:")
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

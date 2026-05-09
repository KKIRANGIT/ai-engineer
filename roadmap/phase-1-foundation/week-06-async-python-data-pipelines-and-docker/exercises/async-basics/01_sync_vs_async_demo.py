"""
Week 06 - Async Basics: Why waiting time matters

This file compares a synchronous sequence with an asynchronous one.
"""

import asyncio
import time


def sync_fetch(label, delay_seconds):
    """Simulate a blocking I/O operation."""
    time.sleep(delay_seconds)
    return f"{label} finished after {delay_seconds} seconds"


async def async_fetch(label, delay_seconds):
    """Simulate a non-blocking I/O wait."""
    await asyncio.sleep(delay_seconds)
    return f"{label} finished after {delay_seconds} seconds"


def run_sync_version():
    """Run two blocking waits one after another."""
    start_time = time.perf_counter()
    first_result = sync_fetch("first task", 1)
    second_result = sync_fetch("second task", 1)
    elapsed_seconds = time.perf_counter() - start_time

    print("Sync results:")
    print(first_result)
    print(second_result)
    print(f"Sync total time: {elapsed_seconds:.2f} seconds")


async def run_async_version():
    """Run two waiting tasks so their wait time overlaps."""
    start_time = time.perf_counter()
    first_task = asyncio.create_task(async_fetch("first task", 1))
    second_task = asyncio.create_task(async_fetch("second task", 1))
    results = await asyncio.gather(first_task, second_task)
    elapsed_seconds = time.perf_counter() - start_time

    print("Async results:")
    for result in results:
        print(result)
    print(f"Async total time: {elapsed_seconds:.2f} seconds")


def main():
    """Run both versions for comparison."""
    run_sync_version()
    print("-" * 40)
    asyncio.run(run_async_version())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Measure the runtime of parallel asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Run four async comprehensions concurrently and return elapsed time."""
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    return time.perf_counter() - start_time

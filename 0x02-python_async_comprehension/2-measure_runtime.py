#!/usr/bin/env python3
""" coroutine that will execute async_comprehension """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ run async_comprehension 4 times and return time elapsed """
    start_time = time.time()
    asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - start_time

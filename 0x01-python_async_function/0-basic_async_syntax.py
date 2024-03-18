#!/usr/bin/env python3
""" asynchronous coroutine that waits for a random delay """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for a random delay between 0, max_delay and return """
    random_delay: float = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(random_delay)
    return random_delay

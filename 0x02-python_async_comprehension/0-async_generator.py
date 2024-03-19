#!/usr/bin/env python3
""" async generator """
import asyncio
import random
from typing import Generator, Float


async def async_generator() -> Generator[Float, None, None]:
    """ wait 1 sec then yield random number """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

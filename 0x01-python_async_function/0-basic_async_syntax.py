#!/usr/bin/python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay (inclusive) and returns it."""
    delay = random.uniform(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Wait asynchronously for the generated delay
    return delay

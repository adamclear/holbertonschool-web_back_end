#!/usr/bin/env python3
''' This is an asyncronous function that takes an int as an argument
(max_delay (default 10)), waits a random amount of seconds between
0 - max_delay, and then returns the amount of time delayed. '''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' Uses random.uniform() to generate a delay and then
        returns that delay value after waiting for that time. '''
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

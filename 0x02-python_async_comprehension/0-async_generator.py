#!/usr/bin/env python3
''' This coroutine runs 10 times. Each time it waits 1 second and then
yields a random number between 0 and 10. '''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generates a number between 0 - 10 using random. 10 times.'''
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

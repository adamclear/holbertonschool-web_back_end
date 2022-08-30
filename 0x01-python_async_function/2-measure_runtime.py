#!/usr/bin/env python3
''' This function measures the amount of time it takes to run wait_n using
the given n number of times to run wait_random and the given max_delay. '''

import asyncio
import time
wait_n = __import__('1-concurrent-coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Uses asyncio to run wait_n using the given variables and uses
    time to measure the amount of time it takes to run. '''
    startTime: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime: float = time.time()
    return (endTime - startTime) / n

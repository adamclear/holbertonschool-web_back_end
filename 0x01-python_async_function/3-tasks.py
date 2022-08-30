#!/usr/bin/env python3
''' This function asyncio to return a task of wait_random with the given
max_delay. '''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Returns ansyncio task of wait_random '''
    return asyncio.create_task(wait_random(max_delay))

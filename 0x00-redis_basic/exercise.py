#!/usr/bin/env python3
''' Redis file for tasks '''


import redis
from typing import Callable, Union
import uuid


class Cache():
    ''' Caching class '''
    def __init__(self):
        ''' Init method '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Data storage '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        ''' Retrieve data from cache and convert back to type '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        ''' Gets str type data from cache '''
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        ''' Gets int type data from cache '''
        return self.get(key, int)

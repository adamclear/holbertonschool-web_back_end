#!/usr/bin/env python3
''' Redis file for tasks '''


import redis
from typing import Union
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

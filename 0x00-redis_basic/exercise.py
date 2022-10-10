#!/usr/bin/env python3
''' Redis file for tasks '''


from functools import wraps
import redis
from typing import Callable, Union
import uuid


def count_calls(method: Callable) -> Callable:
    ''' Increments the number of calls to a method '''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        ''' Counter wrapper '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)

    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Stores method call history '''
    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        ''' History wrapper '''
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    ''' Shows method call history '''
    reDis = redis.Redis()
    qualName = method.__qualname__
    inputs = reDis.lrange(f"{qualName}:inputs", 0, -1)
    outputs = reDis.lrange(f"{qualName}:outputs", 0, -1)
    print(f"{qualName} was called {len(inputs)} times:")
    for inPut, outPut in zip(inputs, outputs):
        print(f"{qualName}(*{(inPut).decode('utf-8')})\
              -> {(outPut).decode('utf-8')}")


class Cache():
    ''' Caching class '''
    def __init__(self):
        ''' Init method '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

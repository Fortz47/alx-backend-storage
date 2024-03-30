#!/usr/bin/env python3
"""creats a cache class thats connects to a redis db"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(func: Callable) -> Callable:
    """counts how many times methods of Cache class are called"""
    key = func.__qualname__

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return func(self, *args, **kwargs)
    return wrapper


class Cache:
    """creats a cache class thats connects to a redis db"""
    count = 0
    def __init__(self):
        """initialize the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """"store item in db"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """Retrieve data from db"""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """Retrieve string data from db"""
        fn = lambda x: x.decode("utf-8")
        return self.get(key, fn)

    def get_int(self, key: str) -> str:
        """Retrieve integer data from db"""
        return self.get(key, int)

#!/usr/bin/env python3
"""creats a cache class thats connects to a redis db"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def replay(func: Callable) -> None:
    """display the history of calls of a particular function"""
    f_name = func.__qualname__
    _redis = redis.Redis()
    print(f"{f_name} was called {int(_redis.get(f_name))} times:")
    inputs = f'{method.__qualname__}:inputs'
    outputs = f'{method.__qualname__}:outputs'
    zipped = zip(_redis.get(inputs), _redis.get(outputs))
    for input, output in zipped:
        print(f"{f_name}(*{input}) -> {output}")
        

def call_history(method: Callable) -> Callable:
    """stores the input and output of a function call to a resis list"""
    keyInputs = f'{method.__qualname__}:inputs'
    keyOutputs = f'{method.__qualname__}:outputs'

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(keyInputs, str(args))
        output = method(self, *args)
        self._redis.rpush(keyOutputs, str(output))
        return output
    return wrapper
        


def count_calls(method: Callable) -> Callable:
    """counts how many times methods of Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """creats a cache class thats connects to a redis db"""
    count = 0
    def __init__(self):
        """initialize the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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

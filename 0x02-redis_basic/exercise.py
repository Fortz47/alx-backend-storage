#!/usr/bin/env python3
"""creats a cache class thats connects to a redis db"""
import redis
from uuid import uuid4


class Cache:
    """creats a cache class thats connects to a redis db"""
    def __init__(self):
        """initialize the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """"store item in db"""
        id = str(uuid4())
        self._redis.mset({id: data})
        return id

     def get(self, key, fn=None):
        """Retrieve data from db"""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key):
        """Retrieve string data from db"""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key):
        """Retrieve integer data from db"""
        return self.get(key, fn=int)

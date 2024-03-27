#!/usr/bin/env python3
"""creats a cache class thats connects to a redis db"""
import redis
from uuid import uuid4


class Cache:
    """creats a cache class thats connects to a redis db"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        id = str(uuid4())
        self._redis.set(id, data)
        return id

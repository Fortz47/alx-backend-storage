#!/usr/bin/env python3
"""creats a cache class thats connects to a redis db"""
import redis
from uuid import uuid4


class Cache:
    """creats a cache class thats connects to a redis db"""
    def __init__():
        _redis = redis.Redis()
        _redis.flushdb()

    def store(data):
        id = uuid4()
        self._redis.set(id, data)
        return id

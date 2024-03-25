#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    newDoc = Dict(**kwargs)
    res = mongo_collection.insert_one(newDoc)
    return res.inserted_id

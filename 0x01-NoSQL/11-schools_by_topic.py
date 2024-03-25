#!/usr/bin/env python3
"""returns list of school having specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns list of school having specific topic"""
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return list(schools)

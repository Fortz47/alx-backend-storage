#!/usr/bin/env python3
"""returns list of school having specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns list of school having specific topic"""
    schools = mongo_collection.find()
    res = []
    for sch in schools:
        if hasattr(sch, 'topic') and isinstance(sch.topic, str):
            if topic in sch.topic:
                res.append(sch)
    return res

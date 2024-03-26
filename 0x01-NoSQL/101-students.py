#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    students = mongo_collection.find()
    for student in students:
        topics = student.get('topics', [])
        averageScore = sum(i.get('score', 0) for i in topics) / len(topics)
        update = {'$set': {'averageScore': averageScore}}}
        mongo_collection.update_one({'_id': student['_id']}, update)
    return mongo_collection.find().sort('averageScore', -1)

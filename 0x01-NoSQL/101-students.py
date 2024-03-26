#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    students = mongo_collection.find()
    for student in students:
        topics = student.get('topics', [])
        val = sum(1 for i in topics if i['score'] and i['score'] >= 0)
        averageScore = sum(i['score'] for i in topics if i['score'] and i['score'] >= 0) / val
        update = {'$push' : {'topics': {'averageScore': averageScore}}}
        mongo_collection.update_one({'_id': student['_id']}, update)
    return mongo_collection.find().sort('averageScore', -1)

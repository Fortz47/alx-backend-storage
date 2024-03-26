#!/usr/bin/env python3
"""returns all students sorted by average score"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    students = mongo_collection.find()
    for student in students:
        val = sum(1 for i in student.topics if i.score and i.score >= 0)
        averageScore = sum(i.score for i in student.topics if i.score and i.score >= 0) / val
        mongo_collection.update({'_id': student._id}, {$push : {'topics': {'averageScore': averageScore}}})
    return mongo_collection.find()

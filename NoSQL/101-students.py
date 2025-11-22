#!/usr/bin/env python3
"""A script to get top students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by their average score"""

    result = []

    students = mongo_collection.find()

    for student in students:
        topics = student.get('topics', [])
        if topics:
            total = sum(topic.get('score', 0) for topic in topics)
            avg = total / len(topics)
        else:
            avg = 0
        student_with_avg = dict(student)
        student_with_avg['averageScore'] = avg
        result.append(student_with_avg)

    result.sort(key=lambda s: s['averageScore'], reverse=True)

    return result

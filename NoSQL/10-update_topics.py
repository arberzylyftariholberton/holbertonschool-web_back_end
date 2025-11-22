#!/usr/bin/env python3
"""A script that updates all documents"""

def update_topics(mongo_collection, name, topics):
    """
    A function that updates all documents with a
    given school name by setting their topics.
    """

    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

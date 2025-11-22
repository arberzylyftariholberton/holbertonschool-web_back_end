#!/usr/bin/env python3
"""A script that inserts a new doc in a collection"""


def insert_school(mongo_collection, **kwargs):
    """
    A function that returns a new document in a MongoDB collection.
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id

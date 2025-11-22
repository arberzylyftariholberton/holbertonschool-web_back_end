#!/usr/bin/env python
"""A script that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    A function that returns all documents in a MongoDB collection.
    """

    if mongo_collection is None:
        return []

    return list(mongo_collection.find())

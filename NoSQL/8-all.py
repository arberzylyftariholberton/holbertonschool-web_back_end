#!/usr/bin/env python3
"""A script that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    A function that returns all documents in a MongoDB collection.
    """

    return mongo_collection.find()

#!/usr/bin/env python3
"""Display summarized statistics from Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def print_nginx_statistics(collection):
    """ Function that prints total logs, method counts
    and GET /status hits.
    """

    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods: ")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_coll = client.logs.nginx
    print_nginx_statistics(nginx_coll)

#!/usr/bin/env python3
"""Display summarized statistics from Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def summarize_nginx_logs(nginx_coll):
    """ Function that prints total logs, method counts
    and GET /status hits.
    """

    total_entries = nginx_coll.count_documents({})
    print(f"{total_entries} logs")

    print("Methods:")
    methods_to_check = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods_to_check:
        num_requests = nginx_coll.count_documents({"method": m})
        print(f"\tmethod {m}: {num_requests}")

    status_hits = nginx_coll.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_hits} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    summarize_nginx_logs(nginx_collection)

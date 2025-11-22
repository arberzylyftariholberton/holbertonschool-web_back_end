#!/usr/bin/env python3
"""Display stats about Nginx logs, including top 10 IPs"""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(nginx_coll):
    """Print stats for Nginx logs"""

    total_logs = nginx_coll.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    for method in METHODS:
        count = nginx_coll.count_documents({"method": method})
        print(f"    method {method}: {count}")

    status_hits = nginx_coll.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_hits} status check")

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = nginx_coll.aggregate(pipeline)

    print("IPs:")
    for ip in top_ips:
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)

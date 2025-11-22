# debug_repr.py
from pymongo import MongoClient

c = MongoClient("mongodb://127.0.0.1:27017").logs.nginx
total = c.count_documents({})
lines = [f"{total} logs", "Methods:"]
for m in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    lines.append(f"    method {m}: {c.count_documents({'method': m})}")
lines.append(f"{c.count_documents({'method':'GET','path':'/status'})} status check")

for line in lines:
    print(repr(line))

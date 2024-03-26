#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def get_logs():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    documentCount = db.nginx.count_documents({})
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methodDict = {k: db.nginx.count_documents({'method': k}) for k in method}
    status_count = db.nginx.count_documents({"method": "GET", "path": "/status"})
    print(f'{documentCount} logs\nMethods:')
    print(f'\tmethod GET: {methodDict["GET"]}')
    print(f'\tmethod POST: {methodDict["POST"]}')
    print(f'\tmethod PUT: {methodDict["PUT"]}')
    print(f'\tmethod PATCH: {methodDict["PATCH"]}')
    print(f'\tmethod DELETE: {methodDict["DELETE"]}')
    print(f'{status_count} status check')
    ips = db.nginx.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    print('IPs:')
    for ip in ips:
        _ip = ip.get('_id')
        count = ip.get('count')
        print(f'{_ip}: {count}')


if __name__ == '__main__':
    get_logs()

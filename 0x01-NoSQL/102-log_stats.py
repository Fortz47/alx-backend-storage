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
    ipList = [doc.get('ip') for doc in db.nginx.find() if doc.get('ip')]
    ips = set(ipList)
    count = db.nginx.count_documents
    ipDict = {k: count({'ip': k}) for k in ips}
    # creates list of tuple [(k, v)]
    sortedIps = sorted(ipDict.items(), key=lambda x: x[1], reverse=True)
    print('IPs:')
    for i in range(10):
        if sortedIps[i]:
            print(f'{sortedIps[i][0]}: {sortedIps[i][1]}')


if __name__ == '__main__':
    get_logs()

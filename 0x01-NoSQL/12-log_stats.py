#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def get_stats():
    """provides some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    documentCount = db.nginx.count_documents({})
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methodDict = {k: db.nginx.count_documents({'method': k}) for k in method}
    status_count = db.nginx.count_documents({path: "/status"})
    result = f'{documentCount} logs\n \
    Methods:\n \
    \tmethod GET: {methodDict["GET"]}\n \
    \tmethod POST: {methodDict["POST"]}\n \
    \tmethod PUT: {methodDict["PUT"]}\n \
    \tmethod PATCH: {methodDict["PATCH"]}\n \
    \tmethod DELETE: {methodDict["DELETE"]}\n \
    {status_count} status check\n'

get_stats()

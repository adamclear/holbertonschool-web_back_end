#!/usr/bin/env python3
''' Provides stats about Nginx logs stored in MongoDB '''

from pymongo import MongoClient


def log_stats():
    ''' Provides stats about Nginx logs stored in MongoDB '''
    logs = MongoClient().logs.nginx
    print(f"{logs.count_documents({})} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    print(f"{logs.count_documents({'method': 'GET', 'path': '/status'})}\
        status check")


if __name__ == "__main__":
    log_stats()

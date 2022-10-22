#!/usr/bin/env python3
''' Lists all documents in a mongodb collection '''


def list_all(mongo_collection):
    ''' Lists all documents in a mongodb collection '''
    docList = []
    for doc in mongo_collection.find():
        docList.insert(doc)
    return docList

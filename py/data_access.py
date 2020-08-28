import sys

import bson
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.operations import *


class DataAccess():
    def __init__(self, uri= 'mongodb://localhost:27017'):
        super().__init__()
        self.MONGO_URI = uri

    def getCollection(self):
        client = MongoClient(self.MONGO_URI)
        return client.test.demo

    def insert(self, doc):
        DataAccess.ensure_dict(doc)
        collection = self.getCollection()
        return collection.insert_one(doc)

    def find(self, filter = {}):
        collection = self.getCollection()
        return collection.find(filter)

    @staticmethod
    def ensure_dict(doc):
        if doc and  isinstance(doc,dict): return
        raise ValueError('doc must be a dict with values')

#!/usr/bin/env python3
# ========================
# BHHT Create Tests Script
# ========================
#
# Simple tests checking data coherence etc.
#
import zlib
from pymongo import MongoClient
from config import MONGODB

mongo_client = MongoClient(MONGODB['host'], MONGODB['port'])
db = mongo_client.bhht
collection = db.people

doc = collection.find_one({'html': {'$exists': True}})

compressed = doc['html']
uncompressed = zlib.decompress(doc['html']).decode('utf-8')

print('Size compressed', len(compressed))
print('Size uncompressed', len(uncompressed))
from pymongo import MongoClient
import time
from datetime import datetime

class MongoDBQuery:
    def __init__(self, uri, database, collection):
        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def query(self, filter_query):
        start_time = time.time()
        result = list(self.collection.find(filter_query))
        end_time = time.time()
        print(f"MongoDB query result: {len(result)} rows, query Time: {end_time - start_time:.4f} seconds")
        return result
    
# MongoDB credentials and connection details
username = "root"
password = "mypassword"
database = "jobs"
collection = "jobs"
host = "localhost"
port = "27017"

# Construct the MongoDB URI with credentials
mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/{database}.{collection}?authSource=admin"

# Initialize MongoDB Query
mongo_query = MongoDBQuery(uri=mongo_uri, database=database, collection=collection)


filter_query = {"jobs.dbInsertTimestamp": {"$lt": datetime(2024, 11, 4)}}


mongo_results = mongo_query.query(filter_query=filter_query)
# MongoDB query result: 266126 rows, query Time: 87.1977 seconds
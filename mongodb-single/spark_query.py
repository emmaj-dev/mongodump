from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

class SparkMongoQuery:
    def __init__(self, spark_session, database, collection):
        self.database = database

        self.collection = collection

        self.spark_session = spark_session

    def query(self, filter_condition):
        start_time = time.time()
        df = self.spark_session.read.format("mongodb") \
            .option("database", self.database) \
            .option("collection", self.collection) \
            .option("uri", mongo_uri) \
            .load() \
            .filter(filter_condition)
        
        # Apply filter
        result_df = df.select("_id", "extra")
        result = result_df.collect()  # Force computation and collect results
        end_time = time.time()
        print(f"Query result: {len(result)} rows, Query Time: {end_time - start_time:.4f} seconds")
        return result
    
# MongoDB credentials and connection details
username = "root"
password = "mypassword"
database = "jobs"
collection = "jobs"
host = "mongodb"
port = "27017"

# Construct the MongoDB URI with credentials
mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/{database}.{collection}?authSource=admin"


# Spark Session
myspark = SparkSession \
            .builder \
            .appName("myApp") \
            .config("spark.mongodb.read.connection.uri", mongo_uri) \
            .config("spark.mongodb.write.connection.uri", mongo_uri) \
            .getOrCreate()

# # Initialize Spark Query
spark_query = SparkMongoQuery(spark_session=myspark, database=database, collection=collection)

# Filter Condition
filter_condition = col("jobs.dbInsertTimestamp") < "2024-11-04T00:00:00"
# Query result: 266126 rows, Query Time: 216.5592 seconds


# Run Queries and Compare Times
spark_results = spark_query.query(filter_condition=filter_condition)


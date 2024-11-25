from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# MongoDB credentials and connection details
username = "root"
password = "mypassword"
database = "jobs"
collection = "jobs"
host = "mongodb"
port = "27017"

# Construct the MongoDB URI with credentials
mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/{database}.{collection}?authSource=admin"
# mongo_uri = f"mongodb://{username}:{password}@{host}:{port}/{database}.{collection}"


my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config("spark.mongodb.read.connection.uri", mongo_uri) \
    .config("spark.mongodb.write.connection.uri", mongo_uri) \
    .getOrCreate()

# Load data from MongoDB
df = my_spark.read.format("mongodb") \
    .option("database", "jobs") \
    .option("collection", "jobs") \
    .load()
# Print schema to inspect structure
df.printSchema()
df.show()
from pymongo import MongoClient

# MongoDB connection details
username = "root"
password = "mypassword"
host = "localhost"
port = "27017"
database = "jobs"

try:
    # Create a client and connect
    uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
    client = MongoClient(uri)

    # Test connection
    db = client[database]
    print("Collections in database:", db.list_collection_names())
    print("Connection successful!")

except Exception as e:
    print("Connection failed:", e)

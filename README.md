# mongodump

## Run Direct Query throught MongoDB
paste the command in the terminarl under mongodb-single directory

```python mongo_query.py```

## Run Direct Query throught Spark
paste the command in the terminarl under mongodb-single directory

everytime the query condition is updated, spark_query.py is needed to copy to spark container

```docker cp ./spark_query.py spark-master:/opt/bitnami/spark/spark_query.py```

run the query on container

```docker-compose exec spark-master spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.12:10.1.1 spark_query.py```

## Query Speed Comparison

- condition:{"$lt": "2024-11-04T00:00:00"}
    - Spark query result: 266126 rows, query time: 216.5592 seconds
     - MongoDB query result: 266126 rows, query time: 87.1977 seconds
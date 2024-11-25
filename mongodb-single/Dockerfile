FROM bitnami/spark:latest

# Copy your script into the container
COPY spark_app.py /opt/bitnami/spark/spark_app.py

# Set the default command to run the Spark application
CMD ["spark-submit", "/opt/bitnami/spark/spark_app.py"]

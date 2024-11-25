#!/bin/bash

# Variables
CONTAINER_NAME="mongodb"  # Replace with your MongoDB container name
DUMP_PATH="./mongo_backup"                # Path to the MongoDB dump folder on your host
DATABASE_NAME="jobs"        # Replace with your target database name
HOST_PORT=27017                   # Replace with your MongoDB host port if different
MONGO_USERNAME="root"             # Replace with MongoDB username (if authentication is enabled)
MONGO_PASSWORD="mypassword"       # Replace with MongoDB password (if authentication is enabled)
AUTH_DB="admin"                   # Authentication database

# Check if Docker is running
if ! docker ps > /dev/null 2>&1; then
  echo "Docker is not running. Please start Docker and try again."
  exit 1
fi

# Check if MongoDB container is running
if ! docker ps | grep -q "$CONTAINER_NAME"; then
  echo "MongoDB container ($CONTAINER_NAME) is not running. Please start the container and try again."
  exit 1
fi

# Copy dump folder into the container
echo "Copying dump data to the MongoDB container..."
docker cp "$DUMP_PATH" "$CONTAINER_NAME:/dump"

# # Run mongorestore inside the container
echo "Running mongorestore inside the container..."
docker exec -it "$CONTAINER_NAME" mongorestore \
  --db "$DATABASE_NAME" \
  --username "$MONGO_USERNAME" \
  --password "$MONGO_PASSWORD" \
  --authenticationDatabase "$AUTH_DB" \
  /dump/"$DATABASE_NAME"

# # Clean up the copied dump folder from the container (optional)
echo "Cleaning up dump folder from the container..."
docker exec -it "$CONTAINER_NAME" rm -rf /dump

# # Confirm completion
# echo "Restore process completed successfully!"

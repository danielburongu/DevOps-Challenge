#!/bin/sh

echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
while ! nc -z $DB_HOST $DB_PORT; do
  echo "PostgreSQL is not ready yet. Retrying in 2 seconds..."
  sleep 2
done

echo "PostgreSQL is up - continuing with command: $@"
exec "$@"

# Use Python 3.10-slim as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat for health checks
RUN apt-get update && apt-get install -y netcat-openbsd

# Copy the entrypoint.sh script and set executable permissions
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy the rest of the application code
COPY . .

# Set the working directory to the Django project folder
WORKDIR /app/todo_project

# Collect static files
RUN python manage.py collectstatic --noinput

# Define the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

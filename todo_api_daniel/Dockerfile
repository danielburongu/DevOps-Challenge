FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y netcat-openbsd postgresql-client && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set working directory for Django project
WORKDIR /app/todo_project

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose Django's default port
EXPOSE 8000

# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

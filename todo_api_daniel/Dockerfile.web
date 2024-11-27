FROM python:3.10-slim

WORKDIR /daniel-todo-project

# Install dependencies
RUN apt-get update && \
    apt-get install -y netcat-openbsd postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure staticfiles directory exists
RUN mkdir -p /daniel-todo-project/staticfiles

# Change to the correct working directory
WORKDIR /daniel-todo-project/todo_project

# Collect static files
RUN if [ -f manage.py ]; then python manage.py collectstatic --noinput; else echo "manage.py not found"; fi

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

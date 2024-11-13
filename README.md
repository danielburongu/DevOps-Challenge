# Django To-Do API i.e DevOps-Challenge 🚀

This project is a Django-based web application integrated with PostgreSQL, Nginx, and Docker. It includes a REST API built with Django Rest Framework and uses Gunicorn as the WSGI server. The application is containerized using Docker and managed using Docker Compose. This guide provides step-by-step instructions on setting up and deploying the application.

---

## 🗂️ Table of Contents
- [Prerequisites](#prerequisites)
- [Environment Variables](#environment-variables)
- [Setting Up and Running the Project](#setting-up-and-running-the-project)
- [Accessing the Application](#accessing-the-application)

---

## 🛠️ Prerequisites
Make sure you have the following installed on your system:
- Docker
- Docker Compose
- Python 3.12+
- Git

---

## 🔑 Environment Variables
Before running the project, create a `.env` file in the root directory.

## 🏃 Setting Up and Running the Project
- Step 1: Clone the Repository
  - git clone https:
  - cd DevOps-Challenge

- Step 2: Build and Run the Docker Containers
 - docker-compose up --build

  ## This command will:

1. Set up a PostgreSQL database container.
2. Run migrations and create a superuser in the Django application.
3. Set up an Nginx container to act as a reverse proxy.

- Step 3: Access the Application
 - Django App: http://localhost:8400
 - Nginx: http://localhost:8500
 - Mailhog: http://localhost:9325

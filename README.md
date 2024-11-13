# Django To-Do API with DevOps Practices

## Project Overview
This project demonstrates building a Django-based To-Do API with DevOps best practices, including containerization using Docker, continuous integration using GitHub Actions, and deployment automation with Ansible.

### Features
- User authentication (registration, login, and logout)
- To-Do task management (CRUD operations)
- PostgreSQL database for data persistence
- Email notifications using MailHog
- Deployed using Docker and Ansible

## Technologies Used
- Django & Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Nginx
- GitHub Actions for CI/CD
- Ansible for deployment automation
- MailHog for email testing

## Getting Started

### Prerequisites
- Python 3.10
- Docker & Docker Compose
- Git
- Ansible (for deployment)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-api-devops.git
    cd todo-api-devops
    ```
2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

### Running the Application
1. Build and run Docker containers:
    ```bash
    docker-compose up --build
    ```
2. Access the application at: [http://localhost](http://localhost).

### Running Tests
```bash
python manage.py test

# 🧪 Technical Challenge – Django Project (1 Hour)

## Overview

As part of this technical evaluation, your task is to **create a Django project from scratch**, using **Docker** to manage and run the services.

The project theme is: **Administration of educational institutions**.

We recommend you start by implementing at least the following core models:

- `Institution` (or `School`) – the main organizational unit
- `Teacher` – representing staff or faculty

After that, you're expected to **continue shaping the system** by designing and adding other models and features you think are necessary for a basic school management system.  
This may include entities like `Student`, `Class`, `Subject`, `Schedule`, or any other component you believe is relevant.

Part of the challenge is to decide **what's important to include** in an MVP for managing an educational institution.

## Requirements

- ✅ Project created using **Django**
- ✅ Setup and run using **Docker** (Dockerfile + docker-compose)
- ✅ Define and implement models and relationships based on the described theme
- ✅ Include at least some minimal **tests** (unit or integration)
- ✅ Code should follow good practices and clear structure

## Time Limit

⏱️ **You have 1 hour** to complete this challenge.

We're not expecting a full-featured application, but we do want to see how you **approach a problem**, structure your code, and make design decisions under time pressure.

## Good luck!

# School Administration System

A Django-based system for managing educational institutions, including teachers, students, classes, and schedules.

## Features

- Institution management
- Teacher management
- Student enrollment
- Class scheduling
- Subject management
- Academic year planning

## Prerequisites

- Docker
- Docker Compose
- Git

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd backend
```

### 2. Environment Setup

The project uses Docker for development and deployment. No local Python installation is required.

### 3. Build and Run the Application

```bash
# Build and start the containers
docker-compose up -d

# The application will be available at:
# http://localhost:8000
```

### 4. Database Setup

The first time you run the application, the database will be automatically created and migrations will be applied. However, if you need to manually set up the database:

```bash
# Apply migrations
docker-compose exec web python manage.py migrate

# Load initial data (optional)
docker-compose exec web python manage.py loaddata initial_data.json
```

### 5. Accessing the Application

- Web Interface: http://localhost:8000
- Admin Interface: http://localhost:8000/admin

To access the admin interface, you first need to create a superuser account:

```bash
# Create a superuser
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials:
- Enter your desired username
- Enter your email address (optional)
- Enter and confirm your password

Once created, you can log in to the admin interface using these credentials.

### 6. Development Commands

```bash
# View logs
docker-compose logs -f

# Create new migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser

# Stop the application
docker-compose down
```

### 7. Database Reset and Migration

If you need to reset the database or make significant changes to the models, follow these steps:

```bash
# Stop all containers and remove volumes (this will delete all data)
docker-compose down -v

# Start the containers again
docker-compose up -d

# Create and apply migrations
docker-compose exec web python manage.py makemigrations core
docker-compose exec web python manage.py migrate

# Load initial data (if needed)
docker-compose exec web python manage.py loaddata initial_data.json
```

Note: The `-v` flag in `docker-compose down -v` will remove all volumes, including the database. Use with caution in production environments.

### 8. Logging System

The application includes a comprehensive logging system that tracks:

- All HTTP requests and responses
- CRUD operations on models
- User activities

Logs are written to:
- Console output (for immediate viewing)
- Rotating log files in the `logs/` directory

#### Logged Information

1. HTTP Requests:
   - Request method and path
   - User making the request
   - IP address
   - Timestamp
   - Response status code

2. Model Operations:
   - Model creation
   - Model updates
   - Model deletions
   - Model type and ID
   - User performing the action
   - Timestamp

#### Viewing Logs

```bash
# View real-time logs from the web container
docker-compose logs -f web

# View the log file directly
cat logs/activity.log
```

The log files are rotated when they reach 5MB, keeping up to 5 backup files.

## Project Structure

```
backend/
├── core/                   # Main application
│   ├── models/            # Database models
│   │   ├── institution.py # Institution model
│   │   ├── teacher.py     # Teacher model
│   │   ├── student.py     # Student model
│   │   ├── academic.py    # Class, Subject, and Schedule models
│   │   ├── enrollment.py  # Enrollment model
│   │   └── __init__.py   # Model imports
│   ├── templates/         # HTML templates
│   ├── fixtures/          # Initial data
│   ├── tests/            # Test files
│   └── views.py          # View controllers
├── school_admin/         # Project configuration
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── Dockerfile          # Docker configuration
└── docker-compose.yml  # Docker Compose configuration
```

## Database Schema

The system includes the following main models:
- Institution
- Teacher
- Student
- Class
- Subject
- Enrollment
- Schedule

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
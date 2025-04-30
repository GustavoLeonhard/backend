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

### 3. Code Organization

The project follows a modular structure where related functionality is grouped together:

- **Models**: Each model is in its own file under `core/models/`
- **URLs**: URL patterns are split by functionality in `core/urls/`
- **Views**: Views are organized by functionality in `core/views/`
- **Forms**: All forms are defined in `core/forms.py`

This modular structure makes the code easier to maintain and scale. For more details, see the [Code Organization](#code-organization) section.

### 4. Build and Run the Application

```bash
# Build and start the containers
docker-compose up -d

# The application will be available at:
# http://localhost:8000
```

### 5. Database Setup

The first time you run the application, the database will be automatically created and migrations will be applied. The initial data will also be loaded automatically. If you need to manually set up the database:

```bash
# Apply migrations
docker-compose exec web python manage.py migrate

# Load initial data (optional)
docker-compose exec web python manage.py loaddata core/fixtures/initial_data.json
```

### 6. Accessing the Application

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

### 7. Development Commands

```bash
# View logs
docker-compose logs -f

# Create new migrations
docker-compose exec web python manage.py makemigrations

# Apply migrations
docker-compose exec web python manage.py migrate

# Stop the application
docker-compose down
```

### 8. Database Reset and Migration

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
docker-compose exec web python manage.py loaddata core/fixtures/initial_data.json
```

Note: The `-v` flag in `docker-compose down -v` will remove all volumes, including the database. Use with caution in production environments.

### 9. Logging System

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
│   ├── urls/              # URL configurations
│   │   ├── institution.py # Institution URLs
│   │   ├── teacher.py     # Teacher URLs
│   │   ├── student.py     # Student URLs
│   │   ├── academic.py    # Academic URLs
│   │   ├── enrollment.py  # Enrollment URLs
│   │   └── __init__.py   # URL imports
│   ├── views/             # View controllers
│   │   ├── institution.py # Institution views
│   │   ├── teacher.py     # Teacher views
│   │   ├── student.py     # Student views
│   │   ├── academic.py    # Academic views
│   │   ├── enrollment.py  # Enrollment views
│   │   └── __init__.py   # View imports
│   ├── templates/         # HTML templates
│   ├── fixtures/          # Initial data
│   ├── tests/            # Test files
│   ├── forms.py          # Form definitions
│   ├── urls.py           # Main URL configuration
│   └── views.py          # Main view (home)
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

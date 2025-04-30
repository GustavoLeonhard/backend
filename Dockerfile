FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make wait-for-postgres.sh executable
RUN chmod +x wait-for-postgres.sh

# Run migrations and start server
CMD ["./wait-for-postgres.sh", "db", "sh", "-c", "python manage.py migrate && gunicorn school_admin.wsgi:application --bind 0.0.0.0:8000"]

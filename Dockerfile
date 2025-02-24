# Use official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the working directory
COPY citizen_institute/ /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port 8000 for Django
EXPOSE 8000

# Run migrations and start Django server
CMD ["sh", "-c", "python /app/manage.py migrate && python /app/manage.py runserver 0.0.0.0:8000"]

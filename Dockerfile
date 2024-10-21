FROM python:3.11

# Set environment variables to prevent .pyc files and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django development server by default
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

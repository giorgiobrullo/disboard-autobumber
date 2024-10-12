# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Install git and other dependencies needed for building Python packages
RUN apt-get update && apt-get install -y git && apt-get clean

# Copy the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to /app
COPY . .

# Define environment variable to prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Run main.py when the container launches
CMD ["python3", "main.py"]

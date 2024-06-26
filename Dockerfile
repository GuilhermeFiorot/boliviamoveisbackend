# Use an official Python runtime as a parent image
FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose ports needed for the application (Flask defaults to 5000)
EXPOSE 5000

# Use gunicorn as the entrypoint, adjust the number of workers and threads as needed
CMD ["gunicorn", "--workers=3", "--threads=3", "-b :5000", "app:app"]

# Optional: Add a label to link back to the source
LABEL org.opencontainers.image.source https://github.com/GuilhermeFiorot/boliviamoveisbackend

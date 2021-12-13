# Dockerfile
# Pull base image
FROM python:3.9
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
RUN pip install pipenv
# Copy project
COPY . /code/
RUN pip install -r requirements.txt
# Expose ports
EXPOSE 8000
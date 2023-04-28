
# Note: This Dockerfile is used to build a container image 
# for a Python web application that uses FastAPI and Uvicorn. 
# The image is based on the official Python 3.10.11-slim-bullseye image. 
# The Dockerfile installs the necessary dependencies and sets up the container 
# to run the application on port 8000 with Uvicorn. 
# The --reload flag enables hot reloading, which is useful during development.

FROM python:3.10.11-slim-bullseye as build-env

RUN pip install --upgrade pip

WORKDIR /app

# Copy the contents of the current directory to the container
COPY . .

# Install the package and its dependencies
RUN pip install .

RUN pip install fastapi uvicorn

EXPOSE 8000

# Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
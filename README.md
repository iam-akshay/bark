# Bark API

The Bark API is a web API that generates waveform prompts from input text. It is built using FastAPI, a modern, fast (high-performance) web framework for building APIs.

## Requirements
- Docker
- Docker Compose

## Running the application
To run the application, follow these steps:

- Clone the repository to your local machine.
- In the project directory, run `docker-compose up --build -d` command.
- Wait for the containers to start. You can monitor the logs using `docker-compose logs -f` command.
- Open your web browser and navigate to http://localhost:8000.
- That's it! The application should now be running in your browser.

## Stopping the application
To stop the application, run `docker-compose down -v` command in the project directory. This will stop and remove all the containers, networks, and volumes created by docker-compose up command.

## Endpoints
The Bark API has two endpoints:

### GET /
This endpoint returns a welcome message.


### POST /api/prompt
This endpoint generates a waveform prompt from the input text.

- Request Body**
The request body must contain a JSON object with two keys:

***text (string):*** any text to be used as input for prompt generation

***filename (string, optional):*** the filename to be used to save the generated prompt. If not provided, a default filename (dummy.npz) will be used.

- Response
If the request is successful, the endpoint will return a JSON object with a message indicating that prompt generation has been started.

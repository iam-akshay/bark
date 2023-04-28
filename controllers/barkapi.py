from config import app, logger
from fastapi import Request
from helpers.general import generate_prompt
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Bark API"}


@app.post("/api/prompt")
async def get_data(request: Request):
    """
    Endpoint to generate a waveform prompt from the input text.

    :body: text: any text
    :body: filename: filename use to save file

    Returns:
        dict: A dictionary containing a message and the filename of the generated prompt.
    """

    data = await request.json()

    filename = data.get("filename", "dummy.npz")
    text = data.get("text", "")

    # Use threading to generate the waveform prompt asynchronously
    executor.submit(generate_prompt, text, filename)

    return {
        "message": "Prompt generation has been started. "
        "You can find the file in the 'prompts' directory."
    }

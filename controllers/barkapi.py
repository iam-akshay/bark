from config import app, logger
from fastapi.responses import JSONResponse
from fastapi import Body
from helpers.general import generate_prompt
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()


@app.get("/")
async def welcome():
    return JSONResponse(content={"message": "Welcome to Bark API"})


@app.post("/api/prompt")
async def api_generate_waveform(
    text: str = Body(...), filename: str = Body(...)
) -> JSONResponse:
    """
    Endpoint to generate a waveform prompt from the input text.

    :body: text: any text
    :body: filename: filename use to save file

    Returns:
        dict: A dictionary containing a message and the filename of the generated prompt.
    """

    # Use threading to generate the waveform prompt asynchronously
    executor.submit(generate_prompt, text, filename)

    return JSONResponse(
        content={
            "message": "Prompt generation has been started. "
            "You can find the file in the 'prompts' directory."
        }
    )

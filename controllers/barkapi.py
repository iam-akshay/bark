import json
from config import app, logger
from fastapi import Request, Response
from helpers.general import generate_prompt
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()


@app.get("/")
async def welcome():
    return Response({"message": "Welcome to Bark API"})


@app.post("/api/prompt")
async def api_generate_waveform(request: Request) -> Response:
    """
    Endpoint to generate a waveform prompt from the input text.

    :body: text: any text
    :body: filename: filename use to save file

    Returns:
        dict: A dictionary containing a message and the filename of the generated prompt.
    """
    try:
        data = await request.json()
    except json.JSONDecodeError as e:
        logger.error(str(e))
        return Response(content={"error": str(e)}, status_code=400)

    filename = data.get("filename", "dummy.npz")
    text = data.get("text", "")

    # Use threading to generate the waveform prompt asynchronously
    executor.submit(generate_prompt, text, filename)

    return Response(
        content={
            "message": "Prompt generation has been started. "
            "You can find the file in the 'prompts' directory."
        }
    )

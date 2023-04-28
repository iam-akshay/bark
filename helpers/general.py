from bark.api import text_to_semantic, save_as_prompt, semantic_to_waveform
from config import logger
import os

def generate_prompt(text, filename):
    """
    Function to generate a waveform prompt from the input text and save it to a file.

    Args:
        text (str): The input text to convert to a waveform prompt.
        filename (str): The filename to save the generated prompt to.
    """
    logger.info("-----PROMPT GENERATING PROCESS STARTED-----")

    semantic = text_to_semantic(text=text)
    semantic_prompt, _ = semantic_to_waveform(
        semantic_tokens=semantic, output_full=True
    )
    try:
        save_as_prompt(os.path.join("/prompt", filename), semantic_prompt)
        logger.info(f"-----PROMPT GENERATED SUCCESSFULLY WITH FILE: {filename}-----")
    except AssertionError as err:
        logger.error("An error occurred while saving npz file", str(err))

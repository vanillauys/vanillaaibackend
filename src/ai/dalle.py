# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import os
import openai
from dotenv import load_dotenv
from typing import Tuple


# ---------------------------------------------------------------------------- #
# --- OpenAI Dalle Image Generator ------------------------------------------- #
# ---------------------------------------------------------------------------- #


load_dotenv()

class DalleAI():


    # ------------------------------------------------------------------------ #
    # --- Dalle Configuration ------------------------------------------------ #
    # ------------------------------------------------------------------------ #


    openai.api_key = os.getenv("OPEN_AI_KEY")
    size = '1024x1024'
    n = 1


    # ------------------------------------------------------------------------ #
    # --- Dalle Image Generator ---------------------------------------------- #
    # ------------------------------------------------------------------------ #


    def generate_image(self, text: str) -> Tuple[int, str, dict]:
        try:
            response = openai.Image.create(
                prompt=self.__prompt(text),
                n=self.n,
                size=self.size
            )
            return 200, f"successfully generated image for '{text}'", response
        except Exception:
            return 500, f"could not generate image for '{text}'", None


    def __prompt(self, text: str) -> str:
        return f"{text}, in a digital art style"

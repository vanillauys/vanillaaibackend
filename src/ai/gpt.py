# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import os
import openai
from dotenv import load_dotenv
from typing import Tuple


# ---------------------------------------------------------------------------- #
# --- OpenAI Davinci Summarizer ---------------------------------------------- #
# ---------------------------------------------------------------------------- #


load_dotenv()

class DavinciAI():


    # ------------------------------------------------------------------------ #
    # --- Davinci Configuration ---------------------------------------------- #
    # ------------------------------------------------------------------------ #


    openai.api_key = os.getenv("OPEN_AI_KEY")
    model = 'text-davinci-003'
    temperature = 0.7
    max_tokens = 2048
    n = 1
    stop = '###'


    # ------------------------------------------------------------------------ #
    # --- Davinci Summarize -------------------------------------------------- #
    # ------------------------------------------------------------------------ #


    def summarize(self, text: str) -> Tuple[int, str, list[str]]:
        try:
            response = openai.Completion.create(
                model=self.model,
                prompt=self.__prompt(text),
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                stop=self.stop
            )
            text_response = response['choices'][0]['text']
            return 200, 'successfully summarized the text.', self.__format_response(text_response)
        except Exception:
            return 500, 'could not summarize the text.', response
    

    def __prompt(self, text:str) -> str:
        prompt = "Summarize the information into a introduction, central idea, conclusion and give 5 key points of the information, into the following format:"
        prompt += "\n\nIntroduction: about 200 words\nCentral idea: about 400 words\nConclusion: about 200 words\nKey points:\n1.\n2.\n3.\n4.\n5."
        prompt += f"\n\n{text}\n###"
        return prompt


    def __format_response(self, text: str) -> list[str]:
        #formatted_text: list[str] = []
        text = text.replace('\\n', '\n')
        return text

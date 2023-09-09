# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import whisper
from schemas import WhisperTranscribeReturnClass as WhisperReturn

# ---------------------------------------------------------------------------- #
# --- OpenAI Whisper Transcriber --------------------------------------------- #
# ---------------------------------------------------------------------------- #


class WhisperAI:
    # ------------------------------------------------------------------------ #
    # --- Whisper Configuration ---------------------------------------------- #
    # ------------------------------------------------------------------------ #

    whisper_model = whisper.load_model("base")

    # ------------------------------------------------------------------------ #
    # --- Whisper Transcriber ------------------------------------------------ #
    # ------------------------------------------------------------------------ #

    def transcribe_audio(self, audio: str) -> WhisperReturn:
        try:
            transcription = self.whisper_model.transcribe(audio, fp16=False)
            return_model: WhisperReturn = {
                "text": str(transcription["text"]),
                "error": False,
            }
        except Exception as e:
            return_model: WhisperReturn = {"text": str(e), "error": True}
        return return_model

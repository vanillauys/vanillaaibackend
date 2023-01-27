# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import whisper


# ---------------------------------------------------------------------------- #
# --- OpenAI Whisper Transcriber --------------------------------------------- #
# ---------------------------------------------------------------------------- #


class WhisperAI():


    # ------------------------------------------------------------------------ #
    # --- Whisper Configuration ---------------------------------------------- #
    # ------------------------------------------------------------------------ #


    whisper_model = whisper.load_model("base")


    # ------------------------------------------------------------------------ #
    # --- Whisper Transcriber ------------------------------------------------ #
    # ------------------------------------------------------------------------ #


    def transcribe_audio(self, audio: str):
        try:
            transcription = self.whisper_model.transcribe(audio, fp16=False)
            return 200, transcription
        except Exception:
            return 500, None

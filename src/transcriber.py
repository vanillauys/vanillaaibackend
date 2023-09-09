# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from schemas import WhisperTranscribeReturnClass as WhisperReturn
from ai.transcribe import WhisperAI
from applogger import log


# ---------------------------------------------------------------------------- #
# --- Transcriber ------------------------------------------------------------ #
# ---------------------------------------------------------------------------- #


def main():
    # TODO: Change the filename to transcribe here
    file_name = "htmx in 100 seconds.mp4"
    file_path = f"videos/{file_name}"
    output_path = f"transcriptions/{file_name.split('.')[0]}.txt"

    log.debug(f"{file_name=}")
    log.debug(f"{file_path=}")
    log.debug(f"{output_path=}")

    whisper = WhisperAI()
    log.debug(f"Transcribing {file_name}... This might take a while.")
    transcription: WhisperReturn = whisper.transcribe_audio(file_path)

    if transcription["error"]:
        log.error(f"Failed to transcribe {file_name}")
        log.error(f"{transcription['text']}")
        return

    log.debug(f"Writing transcription to {output_path}")

    # Write out the contents of the transcription to files
    with open(output_path, "w") as output_file:
        output_file.write(transcription["text"])

    log.debug(f"Successfully written transcription to {output_path}")


if __name__ == "__main__":
    main()

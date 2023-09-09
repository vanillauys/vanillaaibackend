from youtube.youtube import Youtube
from ai.transcribe import WhisperAI
from ai.gpt import DavinciAI
from ai.dalle import DalleAI
from schemas import YoutubeDownloadReturnClass as YoutubeReturn
from schemas import WhisperTranscribeReturnClass as WhisperReturn
from applogger import log


yt = Youtube()
ws = WhisperAI()
dv = DavinciAI()
dl = DalleAI()


def main():
    url: str = "https://www.youtube.com/watch?v=8nHBGFKLHZQ"
    log.debug(f"Downloading `{url}` with YoutubeDownloader")
    video: YoutubeReturn = yt.download_audio(url)

    if video["error"]:
        log.error(f"Error downloading `{url}`")
        log.error(f"{video['message']}")
        return

    log.debug(f"Transcribing {video['title']} with Whisper")
    transcription: WhisperReturn = ws.transcribe_audio(f"videos/{video['title']}")

    if transcription["error"]:
        log.error(f"Error transcribing `{video['title']}`")
        log.error(f"{transcription['text']}")
        return

    code, response, data = dv.summarize(transcription["text"])

    print(code, data)


if __name__ == "__main__":
    main()

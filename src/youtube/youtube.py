# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from pytube import YouTube
from schemas import YoutubeDownloadReturnClass as YoutubeReturn


# ---------------------------------------------------------------------------- #
# --- YouTube Video Downloader ----------------------------------------------- #
# ---------------------------------------------------------------------------- #


class Youtube:
    # ------------------------------------------------------------------------ #
    # --- Youtube Configuration ---------------------------------------------- #
    # ------------------------------------------------------------------------ #

    directory = "videos/"

    # ------------------------------------------------------------------------ #
    # --- Youtube Downloader ------------------------------------------------- #
    # ------------------------------------------------------------------------ #

    def download_audio(self, url: str) -> YoutubeReturn:
        try:
            title = YouTube(url).title + ".mp4"
            video = YouTube(url).streams.filter(only_audio=True).first()
            size = video.filesize_mb
            if size > 2.5:
                return_model: YoutubeReturn = {
                    "message": f"the video '{title}' is too large to process.",
                    "title": "",
                    "error": True,
                }
            video.download(self.directory, filename=title)
            return_model: YoutubeReturn = {
                "message": f"successfully downloaded '{url}'",
                "title": title,
                "error": False,
            }
        except Exception as e:
            return_model: YoutubeReturn = {
                "message": str(e),
                "title": "",
                "error": True,
            }
        return return_model

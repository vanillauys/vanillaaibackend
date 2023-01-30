# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from pytube import YouTube
from typing import Tuple


# ---------------------------------------------------------------------------- #
# --- YouTube Video Downloader ----------------------------------------------- #
# ---------------------------------------------------------------------------- #


class Youtube():


    # ------------------------------------------------------------------------ #
    # --- Youtube Configuration ---------------------------------------------- #
    # ------------------------------------------------------------------------ #


    directory = 'videos/'


    # ------------------------------------------------------------------------ #
    # --- Youtube Downloader ------------------------------------------------- #
    # ------------------------------------------------------------------------ #


    def download_audio(self, url: str) -> Tuple[int, str, str]:
        try:
            title = YouTube(url).title + '.mp4'
            video = YouTube(url).streams.filter(only_audio=True).first()
            size = video.filesize_mb
            if size > 2.5:
                return 507, f"the video '{title}' is too large to process.", None 
            video.download(self.directory, filename=title)
            return 200, f"successfully downloaded '{url}'", title
        except Exception:
            return 500, f"could not download '{url}'", None


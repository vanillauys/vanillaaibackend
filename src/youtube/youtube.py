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
            video = YouTube(url).streams.filter(only_audio=True)
            video.first().download(self.directory, filename=title)
            return 200, f"successfully downloaded '{url}'", title
        except Exception:
            return 500, f"could not download '{url}'", None

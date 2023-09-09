# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import logging


# ---------------------------------------------------------------------------- #
# --- Logger Configuration --------------------------------------------------- #
# ---------------------------------------------------------------------------- #

log = logging.getLogger("applogger")
log.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(levelname)s L%(lineno)d [%(filename)s] %(asctime)s > %(message)s",
    datefmt="%d-%m-%Y %I:%M:%S",
)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)

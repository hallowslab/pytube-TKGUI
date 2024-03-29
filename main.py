import logging
import sys
import tkinter as tk

from pytube_tkgui import __version__, __NAME__
from pytube_tkgui.app import MainApplication
from pytube_tkgui.functions import retrieve_args, setup_logger

if __name__ == "__main__":
    args = retrieve_args()
    if getattr(args, "version", None):
        sys.stdout.write(f"{__NAME__} version: {__version__}")
        sys.exit(0)
    setup_logger(getattr(args, "log_level"))
    logger = logging.getLogger(__name__)
    root = tk.Tk()
    app = MainApplication(root)
    try:
        root.mainloop()
    except Exception as e:
        logger.critical(f"Unhandled exception occurred:", exc_info=1)
        sys.exit(1)

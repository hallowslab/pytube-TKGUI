import argparse
import logging
import textwrap
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError,AgeRestrictedError, MembersOnly, VideoPrivate, VideoRegionBlocked

LOGGER = logging.getLogger(__name__)

def download_videos(text_element):
    contents = text_element.get("1.0", tk.END)
    if len(contents) < 5:
        LOGGER.error("No urls provided")
        messagebox.showerror(
                "Error",
                f"There don't seem to be any urls in the text input:\n{contents}",
        )
        return
    url_list = [item for item in contents.split("\n") if item != ""]
    for url in url_list:
        LOGGER.debug(f"Downloading URL {url}")
        try:
            yt = YouTube(url)
            compat_streams = yt.streams.filter(only_audio=True)
            compat_streams = [
                stream
                for stream in compat_streams
                if getattr(stream, "mime_type", None) == "audio/mp4"
            ]
            # TODO: get the attribute for the bitrate and download the highest one
            compat_streams[-1].download()
        except RegexMatchError:
            LOGGER.error(f"Invalid Youtube url: {url}")
            messagebox.showerror(
                "Error",
                f"The following url does not appear to be from youtube:\n{url}",
            )
        except (AgeRestrictedError, MembersOnly, VideoPrivate, VideoRegionBlocked):
            LOGGER.error(f"You do not have permissions to access: {url}")
            messagebox.showerror(
                "Error",
                f"This video is not available:\n{url}",
            )
        except Exception as e:
            LOGGER.critical(f"Unhandled exception occurred:", exc_info=1)
            messagebox.showerror(
                "Error",
                f"It wasn't possible to download this url:\n{url}\nDue to the following error:\n{e}",
            )
    messagebox.showinfo(
        "Finished", "The process is complete, you may now close the app, or continue to download"
    )

def retrieve_args():
    description = """\
        ######                                         ####### #    #  #####  #     # ### 
        #     # #   # ##### #    # #####  ######          #    #   #  #     # #     #  #  
        #     #  # #    #   #    # #    # #               #    #  #   #       #     #  #  
        ######    #     #   #    # #####  #####  #####    #    ###    #  #### #     #  #  
        #         #     #   #    # #    # #               #    #  #   #     # #     #  #  
        #         #     #   #    # #    # #               #    #   #  #     # #     #  #  
        #         #     #    ####  #####  ######          #    #    #  #####   #####  ### 
        --------------------------------
            Pytube-TKGUI is a graphical user interface for downloading youtube videos
            using pytube
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="Pytube-TKGUI",
        description=textwrap.dedent(description),
    )
    parser.add_argument("-v", "--version", action="store_true", help="Outputs version to console")
    parser.add_argument("-l", "--log-level", default="INFO", help="Changes application log level for debugging")
    return parser.parse_args()

def setup_logger(log_level):
    numeric_level = getattr(logging, log_level.upper(), 20)
    logging.basicConfig(
        format="%(asctime)s - %(name)s >>> %(levelname)s: %(message)s",
        level=numeric_level,
        datefmt="%d/%m/%Y %I:%M:%S %p",
    )
    logging.info(
        "Logging instantiated with log level: %s",
        logging.getLevelName(logging.getLogger().level),
    )

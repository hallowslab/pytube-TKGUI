import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_videos(text_element):
    contents = text_element.get("1.0", tk.END)
    url_list = [item for item in contents.split("\n") if item != ""]
    for url in url_list:
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
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"It wasn't possible to download this url:\n{url}\nDue to the following error:\n{e}",
            )
    messagebox.showinfo(
        "Finished", "The process is complete, you may now close the app"
    )
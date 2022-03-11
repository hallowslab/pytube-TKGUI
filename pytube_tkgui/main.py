from cgi import test
import tkinter as tk
from tkinter import ttk, N, W, E, S, Button, messagebox
from pytube import YouTube

from utils import __version__


def download_videos(text_element):
    contents = text_element.get("1.0", tk.END)
    url_list = [item for item in contents.split("\n") if item != ""]
    for url in url_list:
        print(f"Downloading {url}")
        try:
            yt = YouTube(url)
            compat_streams = yt.streams.filter(only_audio=True)
            compat_streams = [
                stream
                for stream in compat_streams
                if getattr(stream, "mime_type", None) == "audio/mp4"
            ]
            compat_streams[-1].download()
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"It wasn't possible to download this url:\n{url}\nDue to the following error\n{e}",
            )
    messagebox.showinfo(
        "Finished", "The process is complete, you may now close the app"
    )


window = tk.Tk()
window.title("Pytube-TKGUI")
mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

txt_edit = tk.Text(window)
run_btn = Button(window, text="Download", command=lambda: download_videos(txt_edit))

txt_edit.grid(row=0, column=1, sticky="nsew")
run_btn.grid(row=1, column=1, sticky="nsew")

if __name__ == "__main__":
    window.mainloop()

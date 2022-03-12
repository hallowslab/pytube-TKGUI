import tkinter as tk
from tkinter import N, W, E, S, Button

from pytube_tkgui.functions import download_videos


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("Pytube-TKGUI")
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        txt_edit = tk.Text(self)
        run_btn = Button(self, text="Download", command=lambda: download_videos(txt_edit))
        txt_edit.grid(row=0, column=1, sticky="nsew")
        run_btn.grid(row=1, column=1, sticky="nsew")



import tkinter as tk
from tkinter import N, W, E, S, Button

from pytube_tkgui.functions import download_videos


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("Pytube-TKGUI")
        self.initialize()

    def initialize(self):
        self.grid(column=0, row=0)
        self.grid_configure(sticky="nsew")
        txt_edit = tk.Text(self)
        run_btn = Button(
            self, text="Download", command=lambda: download_videos(txt_edit)
        )
        options_btn = Button(
            self, text="Options", command=lambda: download_videos(txt_edit)
        )
        txt_edit.grid(row=0, column=1, sticky="nsew")
        run_btn.grid(row=1, column=1, sticky="nsew")
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=3)
        self.grid_rowconfigure(0,weight=20)
        self.grid_rowconfigure(1,weight=1)

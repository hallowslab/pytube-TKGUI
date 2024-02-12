import tkinter as tk
from tkinter import N, W, E, S, Button, Text

from idlelib.tooltip import Hovertip

from pytube_tkgui.functions import download_videos


class OptionsWindow(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title = "Pytube-Options"
        self.initialize()

    def initialize(self):
        # Set the window size
        self.geometry("500x300")
        
        label = tk.Label(self, text="Options Window")
        label.pack()

        progressive = tk.Label(self, text="Progressive stream")
        progressive.pack()
        _ = Hovertip(progressive, "This is a tooltip", hover_delay=100)


        # Grab the focus 
        self.grab_set()

    # Release the grab when the window is closed
    def destroy(self):
        self.parent.focus_set()
        tk.Toplevel.destroy(self)

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
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
            self, text="Options", command=self.open_options_window
        )
        txt_edit.grid(row=0, column=0, columnspan=2, sticky="nsew")
        run_btn.grid(row=1, column=1, sticky="nsew")
        options_btn.grid(row=1, column=0, sticky="nsew")
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=4)
        self.grid_rowconfigure(0,weight=20)
        self.grid_rowconfigure(1,weight=1)

    def open_options_window(self):
        OptionsWindow(self)
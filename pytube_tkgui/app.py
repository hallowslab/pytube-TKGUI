import tkinter as tk
from tkinter import N, W, E, S, Button

from pytube_tkgui.utils import ToolTip
from pytube_tkgui.functions import download_videos


class OptionsWindow(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        tk.Toplevel.__init__(self,parent, *args, **kwargs)
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
        tooltip = ToolTip(progressive, "This is a tooltip")


        # Grab the focus and set the window to always on top
        self.grab_set()
        #self.attributes('-topmost', 'true')

    # Release the grab when the window is closed
    def destroy(self):
        self.parent.focus_set()
        tk.Toplevel.destroy(self)

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
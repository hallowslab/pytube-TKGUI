import sys
import textwrap
import tkinter as tk
import argparse

from pytube_tkgui.app import MainApplication

from pytube_tkgui import __version__, __NAME__

def retrieve_args():
    description="Graphical user interface for downloading Youtube videos using pytube"
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
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
    '''))
    parser.add_argument("-v", "--version", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = retrieve_args()
    if getattr(args, "version", "none"):
        sys.stdout.write(f"{__NAME__} version: {__version__}")
        sys.exit(0)
    root = tk.Tk()
    MainApplication(root)
    try:
        root.mainloop()
    except Exception as e:
        sys.stdout.write("Critical error: {e}")
        sys.exit(1)
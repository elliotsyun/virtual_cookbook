import tkinter as tk
from MainWindow import *
from NewRecipeWindow import *

# "iPhone-size" according to google lol
WINDOW_GEOMETRY = "375x667"
APP_TITLE = "Good Eats"

class AppController(tk.Tk):
    
    def __init__(self):
        super().__init__()

        # These are always true, and therefore set by the AppController
        self.title(APP_TITLE)
        self.geometry(WINDOW_GEOMETRY)
        self.resizable(False, False)
                
        # container is what "holds" the different Windows
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # all frames will be kept here
        self.frames = {}

        # for each class, initialize new windows with parent=container and container=AppController
        for F in (MainWindow, NewRecipeWindow):
            frame = F(container, self)

            # add the frames to the dictionary by their unique ID
            self.frames[frame.id] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # '1' is the ID of the MainWindow, and we'll want to show that initially
        self.showFrame(1)

    # show frame rearanges the container and shows the Window with id 'id'
    def showFrame(self, id):
        frame = self.frames[id]
        frame.tkraise()
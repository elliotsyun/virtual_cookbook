import tkinter as tk
from GUI.MainFrame import *
from GUI.NewRecipeFrame import *
from GUI.AppFooter import *

APP_TITLE = "Good Eats"

class AppController(tk.Tk):

    def __init__(self):
        super().__init__()

        # These are always true, and therefore set by the AppController, sets window title, size, and disables resizing
        self.title(APP_TITLE)
        self.resizable(True, False)

        # container is what "holds" the different Windows
        container = tk.Frame(self, bd=4, relief="ridge")
        container.pack(fill="both", expand=True)

        # all frames will be kept here (frames = screens)
        self.frames = {}

        # for each class, initialize new windows with parent=container and container=AppController
        for F in (MainFrame, NewRecipeFrame):
            frame = F(container, self)  # create screen

            # add the frames to the dictionary by their unique ID
            self.frames[frame.id] = frame  # save screen using its ID
            frame.grid(row=0, column=0, sticky="nsew")  # place it in the same spot

        # i'm unsure if we want the footer to stay on EVERY window, or if we want it to go away when adding recipes for example
        # self.footer = AppFooter(container, self)

        # '1' is the ID of the MainWindow, and we'll want to show that initially
        self.showFrame(1)

    # show frame rearanges the container and shows the Window with id 'id' (changes which 'screen' is visible)
    def showFrame(self, id):
        frame = self.frames[id]
        frame.tkraise()
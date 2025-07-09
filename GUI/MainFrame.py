import tkinter as tk
from GUI.NewRecipeFrame import *

MAIN_FRAME_ID = 1
class MainFrame(tk.Frame):
    
    # Each window should have
    def __init__(self, parent, controller):
        
        # call the tk.Frame constructor
        super().__init__(parent)
        self.controller = controller
        
        # set the ID of the MainWindow... this will be '1' to allow for a potential error page @ '0'
        self.id = MAIN_FRAME_ID
    
        # test code to display page navigation, clicking the button changes the page to the "NewRecipeWindow"
        tk.Label(self, text="Welcome to the Recipe App", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Add a New Recipe", command=lambda: controller.showFrame(2)).pack()

import tkinter as tk
from MainWindow import *

NEW_RECIPE_WINDOW_ID = 2
class NewRecipeWindow(tk.Frame):
    
    # Each window should have
    def __init__(self, parent, controller):
        
        # call the tk.Frame constructor
        super().__init__(parent)
        self.controller = controller
        
        # set the NewRecipeWindow ID
        self.id = NEW_RECIPE_WINDOW_ID
        
        # test code for outlining page navigation, clicking the button re-displays the MainWindow
        tk.Label(self, text="Add new recipe", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Go back", command=lambda: controller.showFrame(1)).pack()        
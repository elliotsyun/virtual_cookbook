import tkinter as tk
from GUI.NewRecipeFrame import *
from RecipeDatabase import *

# size
MAIN_FRAME_ID = 1
WINDOW_HEIGHT = 667
WINDOW_FOOTER_HEIGHT = 100 # -> the height of the "discover", "add", etc. buttons on the bottom

# color
RECIPE_CONTAINER_COLOR = "lightblue"

class MainFrame(tk.Frame):
    
    # Each window should have
    def __init__(self, parent, controller):
        
        # call the tk.Frame constructor
        super().__init__(parent) # parent = container from the main app
        self.controller = controller
        
        # set the ID of the MainWindow... this will be '1' to allow for a potential error page @ '0'
        self.id = MAIN_FRAME_ID
    
        # test code to display page navigation, clicking the button changes the page to the "NewRecipeWindow"
        self.welcome_test_message = tk.Label(self, text="Welcome to the Recipe App", font=("Arial", 16))
        self.welcome_test_message.grid(row=0, column=2)
        
        self.add_recipe_button = tk.Button(self, text="Add a New Recipe", command=lambda: controller.showFrame(2))
        self.add_recipe_button.grid(row=1, column=2, sticky="nsew")
        
        
        # CODE FOR DISPLAYING RECIPES STARTS HERE (we may want to make this a separate class)

        # Main container frame (light blue)
        self.recipe_container_frame = tk.Frame(self, bg=RECIPE_CONTAINER_COLOR)
        self.recipe_container_frame.grid(row=2, column=2, sticky="nsew")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Add canvas and scrollbar, the part of the window WITHOUT recipes on top of it (fills in the rest of the window)
        canvas = tk.Canvas(self.recipe_container_frame, bg=RECIPE_CONTAINER_COLOR, highlightthickness=0, height=WINDOW_HEIGHT - WINDOW_FOOTER_HEIGHT) # NOTE: Height the bottom buffer should match the size of the buttons on the bottom
        scrollbar = tk.Scrollbar(self.recipe_container_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Internal scrollable frame
        self.scrollable_frame = tk.Frame(canvas, bg=RECIPE_CONTAINER_COLOR)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Embed the frame in the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Allow mousewheel scrolling
        self.scrollable_frame.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # Add recipe frames to scrollable frame
        db = RecipeDatabase()
        for i, recipe in enumerate(db.database):
            recipe.to_frame(self.scrollable_frame, i)
  



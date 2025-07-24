import tkinter as tk
from GUI.NewRecipeFrame import *
from RecipeDatabase import *
from tkinter.font import Font
from Constants import *
from GUI.AppFooter import *
from GUI.AppHeader import *

class MainFrame(tk.Frame):
    
    # Each window should have
    def __init__(self, parent, controller):
        
        # call the tk.Frame constructor
        super().__init__(parent, width=WINDOW_WIDTH, height=WINDOW_HEIGHT) # parent = container from the main app
        self.controller = controller
        
        # set the ID of the MainWindow... this will be '1' to allow for a potential error page @ '0'
        self.id = MAIN_FRAME_ID
    
        # test code to display page navigation, clicking the button changes the page to the "NewRecipeWindow"
        # self.title_font = Font(name="arial", slant="italic")
        # self.welcome_test_message = tk.Label(self, text="Good Eats", font=self.title_font)
        # self.welcome_test_message.grid(row=0, column=2)
        
        # CODE FOR DISPLAYING RECIPES STARTS HERE (we may want to make this a separate class)

        self.header = AppHeader(self, controller)

        # Main container frame (light blue)
        self.recipe_container_frame = tk.Frame(self, bg=RECIPE_CONTAINER_COLOR, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)
        self.recipe_container_frame.grid(row=1, column=0, sticky="nsew")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Add canvas, the part of the window WITHOUT recipes on top of it (fills in the rest of the window)
        canvas = tk.Canvas(self.recipe_container_frame, bg=RECIPE_CONTAINER_COLOR, highlightthickness=0, width=WINDOW_WIDTH, height=(WINDOW_HEIGHT - WINDOW_FOOTER_HEIGHT - HEADER_HEIGHT), bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE) 
        canvas.pack(side="left", fill="both", expand=True)        
        # NOTE: Height the bottom buffer should match the size of the buttons on the bottom
        
        # code for adding PHYSICAL scrollbar to page
        # scrollbar = tk.Scrollbar(self.recipe_container_frame, orient="vertical", command=canvas.yview)
        # canvas.configure(yscrollcommand=scrollbar.set)
        # scrollbar.pack(side="right", fill="y")

        # Internal scrollable frame
        self.scrollable_frame = tk.Frame(canvas, bg=MAIN_RECIPE_BACKGROUND, width=WINDOW_WIDTH, height=(WINDOW_HEIGHT - WINDOW_FOOTER_HEIGHT - HEADER_HEIGHT), bd=TESTING_BORDER_SIZE, relief=TESTING_BORDER_TYPE)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Embed the frame in the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Allow mousewheel scrolling
        self.scrollable_frame.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # load the recipes into the MainFrame scrollable window
        self.load_database_recipes()

        # add the footer to the MainFrame
        self.footer = AppFooter(self, controller)

    def load_database_recipes(self):
        # clear all of the existing recipes
        for recipe in self.scrollable_frame.winfo_children():
            recipe.destroy()

        # load all of the recipes from the database
        db = RecipeDatabase()
        for i, recipe in enumerate(db.database):
            recipe.to_frame(self.scrollable_frame, i)

    # if we just want to add 1 new recipe (i.e on recipe creation) then this is faster
    def load_new_recipe(self, recipe): 
        db = RecipeDatabase()
        recipe.to_frame(self.scrollable_frame, len(db.database))

    def refresh(self):
        self.load_recipes()        
        

  


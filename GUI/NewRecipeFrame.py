import tkinter as tk
from GUI.MainFrame import *
from GUI.AppFooter import *
from Recipe.RatedRecipeDecorator import *
from Recipe.ProteinRecipeDecorator import *
from RecipeDatabase import *

NEW_RECIPE_FRAME_ID = 2
class NewRecipeFrame(tk.Frame):
    
    # Each window should have
    def __init__(self, parent, controller):
        
        # call the tk.Frame constructor
        super().__init__(parent)
        self.controller = controller

        # creating a reference to the RecipeDatabase
        self.recipe_database = RecipeDatabase()
        
        # set the NewRecipeWindow ID
        self.id = NEW_RECIPE_FRAME_ID
        
        tk.Label(self, text="Add new recipe", font=("Arial", 16)).grid(row=0, column=1)
        
        self.title_entry = tk.StringVar(self)
        tk.Label(self, text="title", font=("Arial", 12)).grid(row=2, column=0)
        tk.Entry(self, textvariable=self.title_entry).grid(row=2, column=1) 

        # create a large text box for inputting recipe ingredients... each 'ingredient' should be on a different line (this sucks)
        tk.Label(self, text="ingredients", font=("Arial", 12)).grid(row=3, column=0)
        self.ingredients_entry = tk.Text(self, height=10, width=10)
        self.ingredients_entry.grid(row=3, column=1)    

        # create a large text box for inputting recipe steps
        tk.Label(self, text="steps", font=("Arial", 12)).grid(row=4, column=0)
        self.steps_entry = tk.Text(self, height=10, width=10)
        self.steps_entry.grid(row=4, column=1)                    

        # test code for outlining page navigation, clicking the button re-displays the MainWindow
        tk.Button(self, text="Go back", command=lambda: controller.showFrame(1)).grid(row=5, column=0)    
        tk.Button(self, text="Save recipe", command=self.createNewRecipe).grid(row=5, column=1)
        
    def createNewRecipe(self):
        print("This would create a new recipe")
        
        # unpack the text in the text box... there's a nicer way to input these prolly
        steps = self.steps_entry.get("1.0", 'end-1c').split('\n')
        ingredients = self.ingredients_entry.get("1.0", 'end-1c').split('\n')

        # business logic for creating new recipe
        new_recipe = Recipe(ingredients, steps, self.title_entry.get())

        # testing code
        print(new_recipe)

        # Add the recipe to the database and return the user to the MainFrame
        self.recipe_database.addToDatabase(new_recipe)
        self.controller.showFrame(1)




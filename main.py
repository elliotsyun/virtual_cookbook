import os
import sys
from collections import defaultdict

# file imports
from GUI.AppController import *
from Recipe.RatedRecipeDecorator import *
from Recipe.ProteinRecipeDecorator import *
from RecipeDatabase import *

WINDOW_LENGTH = 375

def main():
    app = AppController()
    app.mainloop()
    
    # after the main loop, write all of the session data to the database
    db = RecipeDatabase()

    rated_recipe = Recipe(['pp1'], ['aa1'], 'rated')
    rated_recipe = RatedRecipeDecorator(rated_recipe, 99)
    db.addToDatabase(rated_recipe)
    rated_recipe = ProteinRecipeDecorator(rated_recipe, 21)
    db.addToDatabase(rated_recipe)    

    db.writeToDatabase()
    

if __name__ == "__main__":
    main()


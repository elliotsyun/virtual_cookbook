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
    db.writeToDatabase()
    

if __name__ == "__main__":
    main()


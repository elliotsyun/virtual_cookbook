from Recipe.Recipe import *

import json
import os
from Recipe.RecipeFactory import RecipeFactory

# ideally we will later transition this to a real database language...
# but since we'll both want to access it, we'll need to hosted somewhere

DATABASE_FILENAME = "RecipeDatabase.json"

# code for setting up Singleton design pattern taken from refactoring.guru
class RecipeDatabaseMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]        


# since this is a Singleton, there will/can only be ONE database
class RecipeDatabase(metaclass=RecipeDatabaseMeta):

    # initialize a database (in this case just a List)
    def __init__(self):

        # if there's already a Database file AND it has Recipes in it... then load
        if os.path.exists(DATABASE_FILENAME) == True and os.path.getsize(DATABASE_FILENAME) > 0:
            self.loadFromDatabase()
        
        # otherwise create a new array
        else:
            self.database = []

        self.printDatabase()

    # add a recipe to the database... in the future this may be an sql operation
    def addToDatabase(self, recipe: Recipe):
        self.database.append(recipe)
        print("added a recipe to the database")

    # printing the database for testing purposes... but its probably easier to look through the json
    def printDatabase(self):
        for recipe in self.database:
            print(recipe)

    # called on program startup, this reads all of the recipes with the help of the RecipeFactory
    def loadFromDatabase(self):
        with open(DATABASE_FILENAME, "r") as f:
            data = json.load(f)
            self.database = [RecipeFactory.from_dict(entry) for entry in data]
        print("Database loaded from JSON.")        

    # dumps all of the recipes that are in the current session to the .json file
    def writeToDatabase(self):
        with open(DATABASE_FILENAME, "w") as f:
            json.dump([r.to_dict() for r in self.database], f, indent=4)
        print("Database written to JSON.")



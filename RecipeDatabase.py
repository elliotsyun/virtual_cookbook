from Recipe.Recipe import *

# ideally we will later transition this to a real database language...
# but since we'll both want to access it, we'll need to hosted somewhere

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
        self.database = []

    # add a recipe to the database... in the future this may be an sql operation
    def addToDatabase(self, recipe: Recipe):
        self.database.append(recipe)
        print("added a recipe to the database")

    # destructor for the RecipeDatabase Singleton... write on program close
    def __del__(self):
        
        # add business logic for writing to database on program termination
        print("Writing to database")

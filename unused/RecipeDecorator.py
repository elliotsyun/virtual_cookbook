from Recipe import *
from Recipe.RecipeFactory import *

# RecipeDecorator allows us to wrap recipes with additional functionality/attributes
class RecipeDecorator(Recipe):
    def __init__(self, recipe: Recipe):
        self.recipe = recipe
    
    # getattr allows us to access "deeper" fields in wrapped objects
    def __getattr__(self, name):
        return getattr(self.recipe, name)

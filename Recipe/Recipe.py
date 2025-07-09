from typing import List
import time

# the recipe class is the most basic recipe possible
class Recipe():

    def __init__(self, ingredients: List[str], steps: List[str], title: str):
        self.ingredients = ingredients
        self.steps = steps
        self.title = title
        
        # timestamp is the time that the original Recipe is created
        self.timestamp = time.time()
        
        # the "fields" is to allow the program to know which fields to display
        self.fields = ["title", "ingredients", "steps", "timestamp"]


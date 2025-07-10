from typing import List
import time

# the recipe class is the most basic recipe possible
class Recipe():

    def __init__(self, ingredients: List[str], steps: List[str], title: str):
        
        # the necessary attributes of ALL recipes
        self.ingredients = ingredients
        self.steps = steps
        self.title = title
        
        # timestamp is the time that the original Recipe is created
        self.timestamp = time.time()
        
        # the "fields" is to allow the program to know which fields to display
        self.fields = ["title", "ingredients", "steps", "timestamp"]

    def __str__(self):
        return self.title + "\n" + str(self.ingredients) + "\n" + str(self.steps)
    
    # converts the Recipe object into Json formatting 
    def to_dict(self):
        return {
            "type": "Recipe",
            "title": self.title,
            "ingredients": self.ingredients,
            "steps": self.steps
        }
    
    # converts the Recipe object BACK FROM Json formatting
    @classmethod
    def from_dict(cls, data):
        return cls(data["ingredients"], data["steps"], data["title"])

from Recipe.RecipeDecorator import *

# RatedRecipeDecorator wraps a Recipe object and adds a "rating" (integer)
class RatedRecipeDecorator(RecipeDecorator):

    def __init__(self, recipe, rating: int):
        super().__init__(recipe)
        self.rating = rating
        self.fields.append("rating")

    # added toString()-esque function for testing recipe contents
    def __str__(self):
        return str(self.recipe) +  "\n" + str(self.rating)




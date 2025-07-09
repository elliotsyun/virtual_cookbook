from Recipe.RecipeDecorator import *

# RatedRecipeDecorator wraps a Recipe object and adds a "rating" (integer)
class RatedRecipeDecorator(RecipeDecorator):

    def __init__(self, recipe, rating: int):
        super().__init__(recipe)
        self.rating = rating
        self.fields.append("rating")




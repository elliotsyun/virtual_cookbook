from Recipe.RecipeDecorator import *

# RatedRecipeDecorator wraps a Recipe object and adds a "rating" (integer)
class RatedRecipeDecorator(RecipeDecorator):

    def __init__(self, recipe, rating: int):
        super().__init__(recipe)
        
        # this implementation of 'rating' is NOT bounded
        self.rating = rating
        self.fields.append("rating")

    # added toString()-esque function for testing recipe contents
    def __str__(self):
        return str(self.recipe) +  "\n" + str(self.rating)
    
    # converts the RatedRecipeDecorator object into Json formatting... recursively calls the inner recipe's to_dict
    def to_dict(self):
        return {
            "type": "RatedRecipeDecorator",
            "rating": self.rating,
            "recipe": self.recipe.to_dict()
        }

    # converts the RatedRecipeDecorator object BACK FROM Json formatting
    @classmethod
    def from_dict(cls, data):
        inner = RecipeFactory.from_dict(data["recipe"])
        return cls(inner, data["rating"])    




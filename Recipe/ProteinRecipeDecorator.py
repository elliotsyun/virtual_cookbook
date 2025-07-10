from Recipe.RecipeDecorator import *

# ProteinRecipeDecorator wraps a Recipe object and adds a "protein amount" (integer)
class ProteinRecipeDecorator(RecipeDecorator):

    def __init__(self, recipe, protein: int):
        super().__init__(recipe)
        self.protein = protein
        self.fields.append("protein")

    # added toString()-esque function for testing recipe contents
    def __str__(self):
        return str(self.recipe) +  "\n" + str(self.protein)  

    # converts the ProteinRecipeDecorator object into Json formatting... recursively calls the inner recipe's to_dict
    def to_dict(self):
        return {
            "type": "ProteinRecipeDecorator",
            "protein": self.protein,
            "recipe": self.recipe.to_dict()
        }

    # converts the RatedRecipeDecorator object BACK FROM Json formatting
    @classmethod
    def from_dict(cls, data):
        inner = RecipeFactory.from_dict(data["recipe"])
        return cls(inner, data["protein"])




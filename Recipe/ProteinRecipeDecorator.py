from Recipe.RecipeDecorator import *

# ProteinRecipeDecorator wraps a Recipe object and adds a "protein amount" (integer)
class ProteinRecipeDecorator(RecipeDecorator):

    def __init__(self, recipe, protein: int):
        super().__init__(recipe)
        self.protein = protein
        self.fields.append("protein")




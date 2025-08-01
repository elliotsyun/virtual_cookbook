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
    
    def to_frame(self, root, placement):
        
        # pending design descisions, this is how you would add text ON TOP of the Recipe to_frame frame
        parent_frame = self.recipe.to_frame(root, placement)
        tk.Label(parent_frame, text=f"{self.protein} protein", font=("Arial", 12), bg=RECIPE_DISPLAY_BACKGROUND_COLOR).pack(anchor="w", padx=10)
        return parent_frame

        # code to override the Recipe to_frame, in case we don't want to keep adding attributes
#        recipe_frame = tk.Frame(root, bg=RECIPE_DISPLAY_BACKGROUND_COLOR, bd=4, relief="ridge")
#        recipe_frame.pack(fill="x", padx=10, pady=10)

#        tk.Label(recipe_frame, text=self.title, font=("Arial", 14, "bold"), bg=RECIPE_DISPLAY_BACKGROUND_COLOR).pack(anchor="w", padx=10, pady=5)
#        tk.Label(recipe_frame, text=f"{len(self.ingredients)} ingredients", font=("Arial", 12), bg=RECIPE_DISPLAY_BACKGROUND_COLOR).pack(anchor="w", padx=10)
#        tk.Label(recipe_frame, text=f"{self.rating} rating", font=("Arial", 12), bg=RECIPE_DISPLAY_BACKGROUND_COLOR).pack(anchor="w", padx=10)       

#        return recipe_frame 




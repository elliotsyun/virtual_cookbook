from Recipe.Recipe import Recipe

# needed a way to read the decorated Recipe objects back from file/database
class RecipeFactory():
    
    # from the json data that is input, it creates a usable python object based on the "type"
    @staticmethod
    def from_dict(data):
        match data["type"]:
            
            case "Recipe":
                return Recipe.from_dict(data)
            
            case "RatedRecipeDecorator":

                # something to keep in mind... I couldn't get this to work without inline imports... kms
                from Recipe.RatedRecipeDecorator import RatedRecipeDecorator
                return RatedRecipeDecorator.from_dict(data)
            
            case "ProteinRecipeDecorator":

                # something to keep in mind... I couldn't get this to work without inline imports... kms
                from Recipe.ProteinRecipeDecorator import ProteinRecipeDecorator
                return ProteinRecipeDecorator.from_dict(data)
            
            case _:
                raise ValueError(f"Unknown recipe type: {data['type']}")
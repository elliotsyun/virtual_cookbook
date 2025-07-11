from Recipe.ProteinRecipeDecorator import *

recipe1 = Recipe([], [], "")
decorated_recipe1 = ProteinRecipeDecorator(recipe1, 0)

recipe2 = Recipe(["1", "2", "3"], ["1", "2", "3"], "test1")
decorated_recipe2 = ProteinRecipeDecorator(recipe2, 9999)

def testProteinRecipeDecoratorConstructor():
    assert decorated_recipe1.title == ""
    assert decorated_recipe1.ingredients == []
    assert decorated_recipe1.steps == []
    assert decorated_recipe1.timestamp != None
    assert decorated_recipe1.fields == ["title", "ingredients", "steps", "timestamp", "protein"]
    assert decorated_recipe1.protein == 0

    assert decorated_recipe2.title == "test1"
    assert decorated_recipe2.ingredients == ["1", "2", "3"]
    assert decorated_recipe2.steps == ["1", "2", "3"]
    assert decorated_recipe2.timestamp != None
    assert decorated_recipe2.fields == ["title", "ingredients", "steps", "timestamp", "protein"]
    assert decorated_recipe2.protein == 9999

def testProteinRecipeDecoratorToDict():
    assert decorated_recipe1.to_dict() == {
        "type": "ProteinRecipeDecorator",
        "protein": 0,
        "recipe": {
            "type": "Recipe",
            "title": "",
            "ingredients": [],
            "steps": []
        }
    }

    assert decorated_recipe2.to_dict() == {
        "type": "ProteinRecipeDecorator",
        "protein": 9999,
        "recipe": {
            "type": "Recipe",
            "title": "test1",
            "ingredients": ['1', '2', '3'],
            "steps": ['1', '2', '3']
        }
    }

def testProteinRecipeToDict():
    empty_data = {
        "type": "ProteinRecipeDecorator",
        "protein": 0,
        "recipe": {
            "type": "Recipe",
            "title": "",
            "ingredients": [],
            "steps": []
        }
    }
    recipe1 = ProteinRecipeDecorator.from_dict(empty_data)
    assert recipe1.title == ""
    assert recipe1.ingredients == []
    assert recipe1.steps == []
    assert recipe1.timestamp != None
    assert recipe1.fields == ["title", "ingredients", "steps", "timestamp", "protein"] 
    assert recipe1.protein == 0   

    nonempty_data = {
        "type": "ProteinRecipeDecorator",
        "protein": 9999,
        "recipe": {
            "type": "Recipe",
            "title": "test1",
            "ingredients": ['1', '2', '3'],
            "steps": ['1', '2', '3']
        }
    }

    recipe2 = ProteinRecipeDecorator.from_dict(nonempty_data)
    assert recipe2.title == "test1"
    assert recipe2.ingredients == ["1", "2", "3"]
    assert recipe2.steps == ["1", "2", "3"]
    assert recipe2.timestamp != None
    assert recipe2.fields == ["title", "ingredients", "steps", "timestamp", "protein"]    
    assert recipe2.protein == 9999
    

def main():
    testProteinRecipeDecoratorConstructor()
    testProteinRecipeDecoratorToDict()
    testProteinRecipeToDict()

if __name__ == "__main__":
    main()    
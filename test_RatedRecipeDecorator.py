from Recipe.RatedRecipeDecorator import *

recipe1 = Recipe([], [], "")
decorated_recipe1 = RatedRecipeDecorator(recipe1, 0)

recipe2 = Recipe(["1", "2", "3"], ["1", "2", "3"], "test1")
decorated_recipe2 = RatedRecipeDecorator(recipe2, 9999)

def testRatedRecipeDecoratorConstructor():
    assert decorated_recipe1.title == ""
    assert decorated_recipe1.ingredients == []
    assert decorated_recipe1.steps == []
    assert decorated_recipe1.timestamp != None
    assert decorated_recipe1.fields == ["title", "ingredients", "steps", "timestamp", "rating"]
    assert decorated_recipe1.rating == 0

    assert decorated_recipe2.title == "test1"
    assert decorated_recipe2.ingredients == ["1", "2", "3"]
    assert decorated_recipe2.steps == ["1", "2", "3"]
    assert decorated_recipe2.timestamp != None
    assert decorated_recipe2.fields == ["title", "ingredients", "steps", "timestamp", "rating"]
    assert decorated_recipe2.rating == 9999

def testRatedRecipeDecoratorToDict():
    assert decorated_recipe1.to_dict() == {
        "type": "RatedRecipeDecorator",
        "rating": 0,
        "recipe": {
            "type": "Recipe",
            "title": "",
            "ingredients": [],
            "steps": []
        }
    }

    assert decorated_recipe2.to_dict() == {
        "type": "RatedRecipeDecorator",
        "rating": 9999,
        "recipe": {
            "type": "Recipe",
            "title": "test1",
            "ingredients": ['1', '2', '3'],
            "steps": ['1', '2', '3']
        }
    }

def testRatedRecipeToDict():
    empty_data = {
        "type": "RatedRecipeDecorator",
        "rating": 0,
        "recipe": {
            "type": "Recipe",
            "title": "",
            "ingredients": [],
            "steps": []
        }
    }
    recipe1 = RatedRecipeDecorator.from_dict(empty_data)
    assert recipe1.title == ""
    assert recipe1.ingredients == []
    assert recipe1.steps == []
    assert recipe1.timestamp != None
    assert recipe1.fields == ["title", "ingredients", "steps", "timestamp", "rating"] 
    assert recipe1.rating == 0   

    nonempty_data = {
        "type": "RatedRecipeDecorator",
        "rating": 9999,
        "recipe": {
            "type": "Recipe",
            "title": "test1",
            "ingredients": ['1', '2', '3'],
            "steps": ['1', '2', '3']
        }
    }

    recipe2 = RatedRecipeDecorator.from_dict(nonempty_data)
    assert recipe2.title == "test1"
    assert recipe2.ingredients == ["1", "2", "3"]
    assert recipe2.steps == ["1", "2", "3"]
    assert recipe2.timestamp != None
    assert recipe2.fields == ["title", "ingredients", "steps", "timestamp", "rating"]    
    assert recipe2.rating == 9999
    

def main():
    testRatedRecipeDecoratorConstructor()
    testRatedRecipeDecoratorToDict()
    testRatedRecipeToDict()

if __name__ == "__main__":
    main()    
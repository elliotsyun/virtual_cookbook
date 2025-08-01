from Recipe.Recipe import *

recipe1 = Recipe([], [], "")
recipe2 = Recipe(["1", "2", "3"], ["1", "2", "3"], "test1")

def testRecipeConstructor():
    assert recipe1.title == ""
    assert recipe1.ingredients == []
    assert recipe1.steps == []
    assert recipe1.timestamp != None
    assert recipe1.fields == ["title", "ingredients", "steps", "timestamp"]

    assert recipe2.title == "test1"
    assert recipe2.ingredients == ["1", "2", "3"]
    assert recipe2.steps == ["1", "2", "3"]
    assert recipe2.timestamp != None
    assert recipe2.fields == ["title", "ingredients", "steps", "timestamp"]

def testRecipeToDict():
    assert recipe1.to_dict() == {'type': 'Recipe', 'title': '', 'ingredients': [], 'steps': []}

    assert recipe2.to_dict() == {'type': 'Recipe', 'title': 'test1', 'ingredients': ['1', '2', '3'], 'steps': ['1', '2', '3']}

def testRecipeFromDict():
    empty_data = {'type': 'Recipe', 'title': '', 'ingredients': [], 'steps': []}
    recipe1 = Recipe.from_dict(empty_data)
    assert recipe1.title == ""
    assert recipe1.ingredients == []
    assert recipe1.steps == []
    assert recipe1.timestamp != None
    assert recipe1.fields == ["title", "ingredients", "steps", "timestamp"]    

    nonempty_data = {'type': 'Recipe', 'title': 'test1', 'ingredients': ['1', '2', '3'], 'steps': ['1', '2', '3']}
    recipe2 = Recipe.from_dict(nonempty_data)
    assert recipe2.title == "test1"
    assert recipe2.ingredients == ["1", "2", "3"]
    assert recipe2.steps == ["1", "2", "3"]
    assert recipe2.timestamp != None
    assert recipe2.fields == ["title", "ingredients", "steps", "timestamp"]    

def main():
    testRecipeConstructor()
    testRecipeToDict()
    testRecipeFromDict()

if __name__ == "__main__":
    main()    
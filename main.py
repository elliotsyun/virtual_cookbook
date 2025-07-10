import os
import sys
from collections import defaultdict

# file imports
from GUI.AppController import *
from Recipe.RatedRecipeDecorator import *
from Recipe.ProteinRecipeDecorator import *
from RecipeDatabase import *


def main():
    app = AppController()
    app.mainloop()

    decorator1 = Recipe(["1", "2"], ["4", "5"], "test")
    # decorator2 = RatedRecipeDecorator(decorator1, 5)
    # decorator3 = ProteinRecipeDecorator(decorator2, 21)
    # print(decorator3.fields)

    # s1 = RecipeDatabase()
    # s2 = RecipeDatabase()
    
    # s1.addToDatabase(decorator1)
    # s2.addToDatabase(decorator1)

    # if id(s1) == id(s2):
    #     print("Singleton works, both variables contain the same instance.")
    # else:
    #     print("Singleton failed, variables contain different instances.")    

    # print("printing")

    # for recipe in s1.database:
    #     print(recipe.title)


    

if __name__ == "__main__":
    main()


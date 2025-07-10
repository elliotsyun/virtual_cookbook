import os
import sys
from collections import defaultdict

# file imports
from GUI.AppController import *
from Recipe.RatedRecipeDecorator import *
from Recipe.ProteinRecipeDecorator import *


def main():
    app = AppController()
    app.mainloop()

    # decorator1 = Recipe(["1", "2"], ["4", "5"], "test")
    # decorator2 = RatedRecipeDecorator(decorator1, 5)
    # decorator3 = ProteinRecipeDecorator(decorator2, 21)
    # print(decorator3.fields)

    

if __name__ == "__main__":
    main()


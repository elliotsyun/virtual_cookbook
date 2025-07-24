import os
import sys
from collections import defaultdict

# file imports
#from GUI.AppController import *
# from Recipe.RatedRecipeDecorator import *
# from Recipe.ProteinRecipeDecorator import *
# from RecipeDatabase import *

from flask import request, jsonify
from config import app, db
from Recipe.Recipe import RecipeObject

WINDOW_LENGTH = 375


    # old frontend
    # app = AppController()
    # app.mainloop()

    # after the main loop, write all of the session data to the database
    # db = RecipeDatabase()
    # db.writeToDatabase()

@app.route("/recipes", methods=["GET"])
def get_recipes():
    recipes = RecipeObject.query.all()
    json_recipes = list(map(lambda x: x.to_json(), recipes))
    return jsonify({"recipes": json_recipes})

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    recipe_title = request.json.get("title")

    if not recipe_title:
        return (
            jsonify({"message": "You must include a recipe title"}),
            400,
        )

    new_recipe = RecipeObject(title=recipe_title)
    try:
        db.session.add(new_recipe)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "Recipe created!"}), 201    

@app.route("/update_recipe/<int:recipe_id>", methods=["PATCH"])
def update_recipe(recipe_id):
    recipe = RecipeObject.query.get(recipe_id)

    if not recipe:
        return jsonify({"message": "Recipe not found"}), 404

    data = request.json
    recipe.title = data.get("title", recipe.title)

    db.session.commit()

    return jsonify({"message": "Recipe updated."}), 200    

@app.route("/delete_recipe/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = RecipeObject.query.get(recipe_id)

    if not recipe:
        return jsonify({"message": "recipe not found"}), 404

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({"message": "recipe deleted!"}), 200

    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


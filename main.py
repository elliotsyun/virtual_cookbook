from flask import request, jsonify
from config import app, db
from Recipe import RecipeObject
import json

# for "Get" requests, we want to get all of the recipes in the database
@app.route("/recipes", methods=["GET"])
def get_recipes():

    # returns a list of all RecipeObject instances
    recipes = RecipeObject.query.all()

    # convert all of the recipes to json by mapping the to_json() function onto them, then convert that to a list (instead of a dict)
    json_recipes = list(map(lambda x: x.to_json(), recipes))

    # convert the list of json_recipes to a proper json response for html
    return jsonify({"recipes": json_recipes})

# a "post" request for creating new recipes in the database
@app.route("/create_recipe", methods=["POST"])
def create_recipe():

    # 
    recipe_title = request.json.get("title")
    recipe_steps = request.json.get("steps")
    recipe_ingredients = request.json.get("ingredients")
    # -> here is where more database fields will be added/prompted for

    # if the user doesn't provide a title, then create an error with error code 400
    if not recipe_title: # && other_fields... etc.
        return (
            jsonify({"message": "You must include a recipe title"}),
            400,
        )

    # otherwise, create a new RecipeObject, with all of the fields provided
    new_recipe = RecipeObject(title=recipe_title, 
                              steps=json.dumps(recipe_steps), 
                              ingredients=json.dumps(recipe_ingredients))


    # try to add it to the database
    try:
        # adding the recipe to the database session only adds it to the "staging" area, we need to commit() to write officially to the database
        db.session.add(new_recipe)
        db.session.commit()

    # if we're unable to write to the database, then return the exception with error code 400
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    # in the case we are successful, return the message "Recipe Created" with code 201
    return jsonify({"message": "Recipe created!"}), 201    

# a "patch" request to update an existing recipe
@app.route("/update_recipe/<int:recipe_id>", methods=["PATCH"])
def update_recipe(recipe_id):

    # the recipe in question that we want to edit, look for it in the database
    recipe = RecipeObject.query.get(recipe_id)

    # if we don't find the recipe in the database, then return an error with error code 404 (not found)
    if not recipe:
        return jsonify({"message": "Recipe not found"}), 404

    # the data in the request from the frontend
    data = request.json

    # if the data contains a title, then replace the recipe's title with the new title, otherwise, keep using the existing title
    recipe.title = data.get("title", recipe.title)
    
    # NOTE: SQLAlchemy cannot have columns with arrays, so array data must be converted to JSON before storing
    if "steps" in data:
        recipe.steps = json.dumps(data["steps"])

    if "ingredients" in data:
        recipe.ingredients = json.dumps(data["ingredients"])

    # push to the database, ensuring the new information is saved
    db.session.commit()

    # return a success message with return code 200
    return jsonify({"message": "Recipe updated."}), 200    

# the "Delete" request for removing recipes from the database
@app.route("/delete_recipe/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):

    # similar to the "patch", check if the recipe exists in the database
    recipe = RecipeObject.query.get(recipe_id)

    if not recipe:
        return jsonify({"message": "recipe not found"}), 404

    # if the recipe exists, then delete it and commit to the database
    db.session.delete(recipe)
    db.session.commit()

    # return a success message
    return jsonify({"message": "recipe deleted!"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)


from config import db
import json

# the recipe class is the most basic recipe possible
class RecipeObject(db.Model):

    # inside the database, each recipe will have an additional "column"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    steps = db.Column(db.Text, unique=False, nullable=False)
    ingredients = db.Column(db.Text, unique=False, nullable=False)


    # convert RecipeObjects to JSON for the frontend
    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "steps": json.loads(self.steps) if self.steps else [],
            "ingredients": json.loads(self.ingredients) if self.ingredients else [],
        }
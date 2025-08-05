from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# ensure that the Flask app has access to the /static 
app = Flask(__name__, static_url_path="/static", static_folder="static")
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
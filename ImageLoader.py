from config import app

# image upload imports
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
DEFAULT_IMAGE_PATH = f"/static/images/default.jpg"

# creates the folder that will contain images, function called immediately by main
def create_upload_folder():
    upload_folder = os.path.join("static", "images", "uploaded")
    os.makedirs(upload_folder, exist_ok=True)
    return upload_folder

# helper function for determining whether a filename is valid
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload_image sets the image to the uploaded image, otherwise it uses the default image
def upload_image(recipe_image):
    # image upload
    if recipe_image and allowed_file(recipe_image.filename):
        filename = secure_filename(recipe_image.filename)
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        recipe_image.save(save_path)
        image_path = f"/static/images/uploaded/{filename}"
    else:
        image_path = DEFAULT_IMAGE_PATH

    return image_path

# if a new_image is entered, then the recipe.image is set, otherwise, nothing is done... this is an attempted edit
def edit_image(new_image, recipe):
    if new_image and allowed_file(new_image.filename):
        filename = secure_filename(new_image.filename)
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        new_image.save(save_path)
        recipe.image = f"/static/images/uploaded/{filename}"
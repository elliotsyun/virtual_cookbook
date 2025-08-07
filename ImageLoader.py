from config import app

# image upload imports
import os
from werkzeug.utils import secure_filename

from PIL import Image

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
DEFAULT_IMAGE_PATH = f"/static/images/default.jpg"

# I'm not sure if 500, 500 is a good quality, but this keeps it kinda not blury
TARGET_IMAGE_SIZE = (500, 500)

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

        resize_image(save_path) # overwrites the full image, not sure if we want this

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

        resize_image(save_path) # overwrites the full image, not sure if we want this

        recipe.image = f"/static/images/uploaded/{filename}"

def resize_image(image_path):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print("File not found")
        return
    
    width, height = img.size
    min_side = min(width, height)

    # Calculate coordinates for a centered crop
    left = (width - min_side) // 2
    top = (height - min_side) // 2
    right = left + min_side
    bottom = top + min_side

    # Crop the center square
    img_cropped = img.crop((left, top, right, bottom))

    # Resize the square crop to the desired size
    img_resized = img_cropped.resize((TARGET_IMAGE_SIZE), Image.LANCZOS)

    img_resized.save(image_path)
    print(f"Image saved to {image_path}")
    

import base64
from database import collection
from PIL import Image
import io

def image_to_base64(image_path):
    """ Convert image to base64 string """
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Example: Store a new image in MongoDB
image_path = "sample_face.jpg"  # Replace with your image file
image_name = "John Doe"  # Name associated with the image

image_base64 = image_to_base64(image_path)

# Insert into MongoDB
collection.insert_one({"name": image_name, "image_base64": image_base64})

print("✅ Image stored successfully in MongoDB Atlas!")

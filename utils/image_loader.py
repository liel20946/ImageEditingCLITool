import sys
from PIL import Image

# Constants
INVALID_IMAGE_PATH = "Invalid Image Path"


def load_image(image_path):
    """
    Load an image from a file path.
    :param image_path: path to the image file.
    :return: the loaded image.
    """
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(INVALID_IMAGE_PATH)

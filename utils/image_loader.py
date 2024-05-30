import sys
from PIL import Image

FILE_NOT_FOUND_MESSAGE = "File not found"


def load_image(image_path):
    # try to load the image
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(FILE_NOT_FOUND_MESSAGE)

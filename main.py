import sys
import numpy as np
from PIL import Image

from utils import load_image
from factories import adjustment_factory, filter_factory

# Constants #

# Error messages
INVALID_COMMAND_MESSAGE = "Invalid command"
INVALID_FILTER_MESSAGE = "Invalid filter"
WRONG_USAGE_MESSAGE = ""  # TODO: fill this in

# Commands
EDIT_COMMAND = "edit_image"
# Edit command parameters
IMAGE_PARAMETER = "--image"
FILTER_PARAMETER = "--filter"
ADJUSTMENT_PARAMETER = "--adjustment"
DISPLAY_PARAMETER = "--display"
SAVE_PARAMETER = "--out"


def display_result(modified_image):
    """
    This function displays the image after all the modifiers have been applied.
    :return: None
    """
    # checks last argument to see if the image should be displayed
    if sys.argv[-1] == DISPLAY_PARAMETER:
        modified_image.show()
    elif sys.argv[-2] == SAVE_PARAMETER:
        modified_image.save(sys.argv[-1])


def create_modifiers_list():
    """
    This function creates a list of modifiers that will be applied to the
    image. the list is created from the command line arguments.
    :return: list of modifiers
    """
    pass


def run_edit_command():
    if len(sys.argv) < 3 or sys.argv[2] != IMAGE_PARAMETER:
        print(WRONG_USAGE_MESSAGE)
        return
    loaded_image = load_image(sys.argv[3])
    if loaded_image is None:
        return

    # create a list of modifiers that will be applied to the image
    modifiers_list = create_modifiers_list()
    # convert the image to a numpy array
    modified_image = np.array(loaded_image)
    # apply the modifiers to the image one after the other
    for modifier in modifiers_list:
        modified_image = modifier.apply(modified_image)
    display_result(Image.fromarray(modified_image))


def run_command():
    if len(sys.argv) > 1 and sys.argv[1] == EDIT_COMMAND:
        run_edit_command()
    # more commands can be added here
    print(INVALID_COMMAND_MESSAGE)


def main():
    run_command()


if __name__ == "__main__":
    main()

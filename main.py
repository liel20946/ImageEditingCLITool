import sys
import numpy as np
from PIL import Image

from utils import load_image
from factories import adjustment_factory, filter_factory

# Constants
INVALID_COMMAND_MESSAGE = "Invalid command"
WRONG_USAGE_MESSAGE = ""  # TODO: fill this in
EDIT_COMMAND = "edit_image"
IMAGE_PARAMETER = "--image"
FILTER_PARAMETER = "--filter"
ADJUSTMENT_PARAMETER = "--adjustment"


def check_edit_arguments_validity():
    pass


def add_filter():
    pass


def add_adjustment():
    pass


def run_edit_command():
    if len(sys.argv) < 3 or sys.argv[2] != IMAGE_PARAMETER:
        print(WRONG_USAGE_MESSAGE)
        return
    loaded_image = load_image(sys.argv[3])
    if loaded_image is None:
        return
    if not check_edit_arguments_validity():
        return


def run_command():
    if len(sys.argv) > 1 and sys.argv[1] == EDIT_COMMAND:
        run_edit_command()
    print(INVALID_COMMAND_MESSAGE)


def main():
    # run_command()
    image = load_image("example_images/dog.jpg")
    image_array = np.array(image)
    c_adjustment = adjustment_factory.create_adjustment("contrast", 2)
    b_adjustment = adjustment_factory.create_adjustment("brightness", 70)
    ed_filter = filter_factory.create_filter("edge_detection")
    b_filter = filter_factory.create_filter("box_blur", 9, 9)
    g_filter = filter_factory.create_filter("grey_scale")
    s_adjustment = adjustment_factory.create_adjustment("saturation", 4)
    image_array = c_adjustment.apply(image_array)
    image = Image.fromarray(image_array)
    image.show()
    # test


if __name__ == "__main__":
    main()

import sys
import numpy as np
from PIL import Image

from factories import adjustment_factory, filter_factory

# Constants #

# Error messages
INVALID_COMMAND = "Invalid Command\n"
INVALID_FILTER = "Invalid Filter\n"
INVALID_ADJUSTMENT = "Invalid Adjustment\n"
INVALID_DISPLAY_ARGUMENT = "Invalid Display Argument\n"
INVALID_IMAGE_PATH = "Invalid Image Path\n"

# Usage message
WRONG_USAGE = ("Usage:\n"
               "edit_image --image <path-to-image> [--filter < "
               "filter-name> --filter-specific_name < "
               "filter-specific_value>]\n"
               "[--adjust <adjustment-name> ‹value>] [--filter < filter-name> "
               "--filter-specific_name < filter-specific_value>]\n"
               "...[--display] [--output <output_path>]")

# Commands
EDIT_COMMAND = "edit_image"
# Edit command parameters
IMAGE_PARAMETER = "--image"
FILTER_PARAMETER = "--filter"
ADJUSTMENT_PARAMETER = "--adjust"
DISPLAY_PARAMETER = "--display"
SAVE_PARAMETER = "--output"


def check_display_method_validity(index):
    arg_size = len(sys.argv)
    return (index == arg_size - 1 and sys.argv[index] == DISPLAY_PARAMETER or
            index == arg_size - 2 and sys.argv[index] == SAVE_PARAMETER)


def display_result(modified_array):
    """
    This function displays the image after all the modifiers have been applied.
    :return: None
    """
    # checks last argument to see if the image should be displayed
    new_image = Image.fromarray(np.uint8(modified_array))
    if sys.argv[-1] == DISPLAY_PARAMETER:
        new_image.show()
    elif sys.argv[-2] == SAVE_PARAMETER:
        new_image.save(sys.argv[-1])
    else:
        print(INVALID_DISPLAY_ARGUMENT)
        print(WRONG_USAGE)


def extract_sub_args(sub_args, start_index, error_message):
    """
    This function gets the arguments for the filter from the command line
    arguments.
    :param error_message: the error message to print if the arguments are.
    :param start_index:  the index of the first argument for the filter in the
    :param sub_args: the arguments for the filter.
    line arguments.
    :return: the arguments for the filter.
    """
    args_values = []
    for i in range(start_index, start_index + 2 * len(sub_args), 2):
        if sys.argv[i] not in sub_args:
            print(error_message)  # TODO: change to more appropriate
            sys.exit(1)
        args_values.append(float(sys.argv[i + 1]))
    return args_values


def check_filter_validity(index, filter_parameters):
    arg_size = len(sys.argv)
    if (index + 1 >= arg_size or sys.argv[index + 1] not in filter_parameters
            or index + 1 + 2 * len(filter_parameters[sys.argv[index + 1]]) >=
            arg_size):
        return False
    return True


def handle_filter_parm(index, filter_parameters, modifiers_list):
    if not check_filter_validity(index, filter_parameters):
        print(INVALID_FILTER)
        print(WRONG_USAGE)
        sys.exit(1)

    filter_name = sys.argv[index + 1]
    filter_args = extract_sub_args(filter_parameters[filter_name],
                                   index + 2,
                                   INVALID_FILTER + '\n' + WRONG_USAGE)

    if len(filter_args) != len(filter_parameters[filter_name]):
        print(INVALID_FILTER)
        print(WRONG_USAGE)
        sys.exit(1)

    new_filter = filter_factory.create_filter(filter_name, *filter_args)
    modifiers_list.append(new_filter)
    return 2 + 2 * len(filter_parameters[filter_name])


def check_adjustment_validity(index, adjustment_set):
    arg_size = len(sys.argv)
    if index + 2 >= arg_size or sys.argv[index + 1] not in adjustment_set:
        return False
    return True


def handle_adjustment_parm(index, adjustment_set, modifiers_list):
    if not check_adjustment_validity(index, adjustment_set):
        print(INVALID_ADJUSTMENT)
        print(WRONG_USAGE)
        sys.exit(1)
    adjustment_type, adjustment_val = (sys.argv[index + 1],
                                       float(sys.argv[index + 2]))
    curr_adjustment = adjustment_factory.create_adjustment(
        adjustment_type, adjustment_val)
    modifiers_list.append(curr_adjustment)
    return 3


def parse_modifier_args(modifiers_list):
    filter_parameters = filter_factory.get_filters_parameters()
    adjustment_set = adjustment_factory.get_adjustments_set()
    i = 4  # start from the first modifier
    arg_size = len(sys.argv)
    while i < arg_size:
        if sys.argv[i] == FILTER_PARAMETER:
            i += handle_filter_parm(i, filter_parameters, modifiers_list)
        elif sys.argv[i] == ADJUSTMENT_PARAMETER:
            i += handle_adjustment_parm(i, adjustment_set, modifiers_list)
        else:
            return i
    return i


def apply_modifiers(modifiers_list, image_array):
    for modifier in modifiers_list:
        image_array = modifier.apply(image_array)
    display_result(image_array)


def load_image(image_path):
    """
    Load an image from a file path.
    :param image_path: path to the image file.
    :return: the loaded image if the path is valid, None otherwise.
    """
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        print(INVALID_IMAGE_PATH)
        return None


def run_edit_command():
    if len(sys.argv) < 3 or sys.argv[2] != IMAGE_PARAMETER:
        print(WRONG_USAGE)
        return

    loaded_image = load_image(sys.argv[3])
    if loaded_image is None: return

    modifiers_list = []
    index = parse_modifier_args(modifiers_list)

    if not check_display_method_validity(index):
        print(INVALID_DISPLAY_ARGUMENT)
        print(WRONG_USAGE)
        return

    apply_modifiers(modifiers_list, np.array(loaded_image))


def run_command():
    if len(sys.argv) > 1 and sys.argv[1] == EDIT_COMMAND:
        run_edit_command()
    # more commands can be added here
    else:
        print(INVALID_COMMAND)
        print(WRONG_USAGE)


def main():
    run_command()


if __name__ == "__main__":
    main()

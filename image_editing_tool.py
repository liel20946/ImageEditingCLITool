import sys
import numpy as np
from PIL import Image
from factories import adjustment_factory, filter_factory

# Constants #

# Error messages
INVALID_COMMAND_MSG = "Invalid Command\n"
INVALID_FILTER_MSG = "Invalid Filter\n"
INVALID_ADJUSTMENT_MSG = "Invalid Adjustment\n"
INVALID_DISPLAY_ARGUMENT_MSG = "Invalid Display Argument\n"
INVALID_IMAGE_PATH_MSG = "Invalid Image Path\n"
INVALID_IMAGE_PARM_MSG = "Invalid Image Parameter\n"
INVALID_FILTER_TYPE_MSG = "Invalid Filter Type\n"
INVALID_ADJUSTMENT_TYPE_MSG = "Invalid Adjustment Type\n"

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


def handle_error(error_message):
    """
    Print the error message and exit the program.
    :param error_message: the error message to print.
    :return: None
    """
    print(error_message)
    print(WRONG_USAGE)
    sys.exit(1)


def check_display_method_validity(index):
    """
    Check if the display method argument is valid.
    :param index: the index of the current argument.
    :return: True if the display method argument is valid, False otherwise.
    """
    arg_size = len(sys.argv)
    return (index == arg_size - 1 and sys.argv[index] == DISPLAY_PARAMETER or
            index == arg_size - 2 and sys.argv[index] == SAVE_PARAMETER)


def display_result(modified_array):
    """
    Display or save the modified image based on user input.
    :param modified_array: the modified image array.
    :return: None
    """
    # checks last argument to see if the image should be displayed
    new_image = Image.fromarray(np.uint8(modified_array))
    if sys.argv[-1] == DISPLAY_PARAMETER:
        new_image.show()
    elif sys.argv[-2] == SAVE_PARAMETER:
        new_image.save(sys.argv[-1])
    else:
        handle_error(INVALID_DISPLAY_ARGUMENT_MSG)


def extract_sub_args(sub_args, start_index, error_message):
    """
    Extract the sub arguments from the command line arguments.
    :param sub_args: dictionary of sub arguments.
    :param start_index: the index to start extracting the sub arguments.
    :param error_message: the error message to print if the sub arguments are
           invalid.
    :return: list of sub arguments values.
    """
    args_values = []
    for i in range(start_index, start_index + 2 * len(sub_args), 2):
        if sys.argv[i] not in sub_args:
            handle_error(error_message)
        args_values.append(float(sys.argv[i + 1]))
    return args_values


def check_filter_validity(index, filter_parameters):
    """
    Check if the filter parameters are valid.
    :param index: index of the filter name in the command line arguments.
    :param filter_parameters: dictionary of filter parameters.
    :return: True if the filter is valid, False otherwise.
    """
    arg_size = len(sys.argv)
    return not (index + 1 >= arg_size or sys.argv[index + 1]
                not in filter_parameters or index + 1 + 2 *
                len(filter_parameters[sys.argv[index + 1]]) >= arg_size)


def handle_filter_parm(index, filter_parameters, modifiers_list):
    """
    Handle parsing the filter parameters.
    :param index: index of current command line argument.
    :param filter_parameters: dictionary of filter parameters.
    :param modifiers_list: list of modifiers to apply to the image.
    :return: the index of the current argument, after parsing the filter
    """
    if not check_filter_validity(index, filter_parameters):
        handle_error(INVALID_FILTER_MSG)

    filter_name = sys.argv[index + 1]
    filter_args = extract_sub_args(filter_parameters[filter_name],
                                   index + 2,
                                   INVALID_FILTER_MSG + '\n' + WRONG_USAGE)

    if len(filter_args) != len(filter_parameters[filter_name]):
        handle_error(INVALID_FILTER_MSG)

    new_filter = filter_factory.create_filter(filter_name, *filter_args)
    if new_filter is None:
        handle_error(INVALID_FILTER_TYPE_MSG)

    modifiers_list.append(new_filter)
    return 2 + 2 * len(filter_parameters[filter_name])


def check_adjustment_validity(index, adjustment_set):
    """
    Check if the adjustment parameters are valid.
    :param index: index of the adjustment name in the command line arguments.
    :param adjustment_set: set of adjustment parameters.
    :return: True if the adjustment is valid, False otherwise.
    """
    arg_size = len(sys.argv)
    return not (index + 2 >= arg_size or sys.argv[index + 1]
                not in adjustment_set)


def handle_adjustment_parm(index, adjustment_set, modifiers_list):
    """
    Handle parsing the adjustment parameters.
    :param index: index of current command line argument.
    :param adjustment_set: set of adjustment parameters.
    :param modifiers_list: list of modifiers to apply to the image.
    :return: the index of the current argument, after parsing the adjustment.
    """
    if not check_adjustment_validity(index, adjustment_set):
        handle_error(INVALID_ADJUSTMENT_MSG)
    adjustment_type, adjustment_val = (sys.argv[index + 1],
                                       float(sys.argv[index + 2]))
    curr_adjustment = adjustment_factory.create_adjustment(
        adjustment_type, adjustment_val)
    if curr_adjustment is not None:
        handle_error(INVALID_ADJUSTMENT_TYPE_MSG)
    modifiers_list.append(curr_adjustment)
    return 3


def parse_modifier_args(modifiers_list):
    """
    Parse the modifiers arguments from the command line.
    :param modifiers_list: list to store the modifiers to apply to the image.
    :return: the index of the current argument, after parsing the modifiers.
    """
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
    """
    Apply the modifiers to the image, one after the other.
    :param modifiers_list: list of modifiers to apply to the image.
    :param image_array: the image to apply the modifiers to.
    :return: the modified image array.
    """
    for modifier in modifiers_list:
        image_array = modifier.apply(image_array)
    return image_array


def load_image(image_path):
    """
    Load the image from the given path.
    :param image_path: the path to the image.
    :return: the loaded image, if it exists.
    """
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        handle_error(INVALID_IMAGE_PATH_MSG)


def run_edit_command():
    """
    Run the edit command, if the arguments are valid.
    :return: None
    """
    if len(sys.argv) < 3 or sys.argv[2] != IMAGE_PARAMETER:
        handle_error(INVALID_IMAGE_PARM_MSG)

    loaded_image = load_image(sys.argv[3])
    if loaded_image is None: return

    modifiers_list = []
    index = parse_modifier_args(modifiers_list)

    if not check_display_method_validity(index):
        handle_error(INVALID_DISPLAY_ARGUMENT_MSG)

    modified_image = apply_modifiers(modifiers_list, np.array(loaded_image))
    display_result(modified_image)


def run_command():
    """
    Run the given command, from the command line arguments.
    :return: None
    """
    if len(sys.argv) > 1 and sys.argv[1] == EDIT_COMMAND:
        run_edit_command()
    # more commands can be added here
    else:
        handle_error(INVALID_COMMAND_MSG)


def main():
    """
    main function to run the program.
    :return: None
    """
    run_command()


if __name__ == "__main__":
    main()

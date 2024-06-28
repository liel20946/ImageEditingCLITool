import sys
import numpy as np
from PIL import Image
from factories import modifier_factory

# Constants #

# Error messages
INVALID_NUMBER_OF_ARGS = "you have entered an invalid number of arguments"
INVALID_COMMAND_MSG = "the entered command is not supported\n"

INVALID_DISPLAY_ARGUMENT_MSG = ("display or save argument not found in the"
                                " correct position\n")
INVALID_IMAGE_PATH_MSG = "couldn't open image, path is invalid\n"
INVALID_IMAGE_TYPE_MSG = "image type is not supported\n"
INVALID_IMAGE_PERMISSION_MSG = "image permission is not valid\n"
INVALID_MIN_ARGS_FOR_EDIT_MSG = "edit command need at least 2 parameters\n"
INVALID_IMAGE_PARM_MSG = "image parameter is not in the correct format\n"

INVALID_MODIFIER_TYPE_MSG = " is an invalid modifier type\n"
INVALID_VALUES_FOR_MODIFIER = ("values for the modifier arguments are not "
                               "valid\n")
MISSING_MODIFIER_ARGUMENT_MSG = "missing modifier arguments\n"
INVALID_MODIFIER_ARGUMENT_MSG = "modifier arguments are not valid\n"
INVALID_NUMBER_OF_ARGS_FOR_MODIFIER = ("invalid number of arguments for "
                                       "modifier\n")

# Usage message
WRONG_USAGE = ("Usage:\n"
               "edit_image --image <path-to-image> [--filter < "
               "filter-name> --filter-specific_name < "
               "filter-specific_value>]\n"
               "[--adjust <adjustment-name> --adjustment-specific_name "
               "‹value>] [--filter < filter-name> "
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

# INDEXES
DISPLAY_IMAGE_INDEX = -1
SAVE_IMAGE_INDEX = -2
SAVE_IMAGE_PATH_INDEX = -1
INPUT_IMAGE_INDEX = 3
COMMAND_INDEX = 1
IMAGE_ARGUMENT_INDEX = 2
MODIFIERS_START_INDEX = 4

# NUMBERS
VALUES_PER_SUB_ARG = 2
NUMBER_OF_ARGS_FOR_SINGLE_ADJUSTMENT = 3
MIN_NUMBER_OF_CLI_ARGS = 2
MIN_NUMBER_OF_EDIT_ARGS = 4


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
    if sys.argv[DISPLAY_IMAGE_INDEX] == DISPLAY_PARAMETER:
        new_image.show()
    elif sys.argv[SAVE_IMAGE_INDEX] == SAVE_PARAMETER:
        new_image.save(sys.argv[SAVE_IMAGE_PATH_INDEX])


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
    end_index = start_index + VALUES_PER_SUB_ARG * len(sub_args)
    for i in range(start_index, end_index, 2):
        if sys.argv[i] not in sub_args or i + 1 >= end_index:
            handle_error(error_message)
        args_values.append(sys.argv[i + 1])
    return args_values


def check_modifier_validity(index, modifier_parameters):
    """
    Check if the modifier parameters are valid.
    :param index: index of the modifier name in the command line arguments.
    :param modifier_parameters: dictionary of modifier parameters.
    :return: None
    """
    arg_size = len(sys.argv)
    if index + 1 >= arg_size:
        handle_error(MISSING_MODIFIER_ARGUMENT_MSG)
    if sys.argv[index + 1] not in modifier_parameters:
        handle_error(sys.argv[index + 1] + INVALID_MODIFIER_TYPE_MSG)
    if (index + 1 + VALUES_PER_SUB_ARG *
            len(modifier_parameters[sys.argv[index + 1]]) >= arg_size):
        handle_error(MISSING_MODIFIER_ARGUMENT_MSG)


def handle_modifier_parm(index, modifier_parameters, modifiers_list):
    """
    Handle parsing the modifier parameters.x
    :param index: index of current command line argument.
    :param modifier_parameters: dictionary of modifier parameters.
    :param modifiers_list: list of modifiers to apply to the image.
    :return: number of arguments to skip after parsing the modifier.
    """
    check_modifier_validity(index, modifier_parameters)
    modifier_name = sys.argv[index + 1]
    modifier_args = extract_sub_args(modifier_parameters[modifier_name],
                                     index + 2, INVALID_MODIFIER_ARGUMENT_MSG)

    if len(modifier_args) != len(modifier_parameters[modifier_name]):
        handle_error(INVALID_NUMBER_OF_ARGS_FOR_MODIFIER)

    new_modifier = modifier_factory.create_modifier(modifier_name,
                                                    *modifier_args)
    if new_modifier is None:
        # since check modifier validity was already called, modifier name
        # is valid, so the error is in the values
        handle_error(INVALID_VALUES_FOR_MODIFIER)

    modifiers_list.append(new_modifier)
    return 2 + VALUES_PER_SUB_ARG * len(modifier_parameters[modifier_name])


def parse_modifier_args(modifiers_list):
    """
    Parse the modifiers arguments from the command line.
    :param modifiers_list: list to store the modifiers to apply to the image.
    :return: the index of the current argument, after parsing the modifiers.
    """
    modifiers_parameters = modifier_factory.get_modifiers_parameters()
    i = MODIFIERS_START_INDEX
    arg_size = len(sys.argv)
    while i < arg_size:
        if sys.argv[i] in {FILTER_PARAMETER, ADJUSTMENT_PARAMETER}:
            i += handle_modifier_parm(i, modifiers_parameters, modifiers_list)
        else:
            break
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
    except TypeError:
        handle_error(INVALID_IMAGE_TYPE_MSG)
    except ValueError:
        handle_error(INVALID_IMAGE_PERMISSION_MSG)


def run_edit_command():
    """
    Run the edit command, if the arguments are valid.
    :return: None
    """
    if len(sys.argv) < MIN_NUMBER_OF_EDIT_ARGS:
        handle_error(INVALID_MIN_ARGS_FOR_EDIT_MSG)
    if sys.argv[IMAGE_ARGUMENT_INDEX] != IMAGE_PARAMETER:
        handle_error(INVALID_IMAGE_PARM_MSG)

    loaded_image = load_image(sys.argv[INPUT_IMAGE_INDEX])
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
    if len(sys.argv) < MIN_NUMBER_OF_CLI_ARGS:
        handle_error(INVALID_NUMBER_OF_ARGS)
    if sys.argv[COMMAND_INDEX] == EDIT_COMMAND:
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

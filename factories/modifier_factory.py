import modifiers
from utils.parameter_check import (check_two_positive_ints,
                                   check_non_negative_float,
                                   check_one_float)

# Constants for the modifier types
BLUR_TYPE = "blur"
EDGE_DETECTION_TYPE = "edge-detection"
SHARPEN_TYPE = "sharpen"
GREY_SCALE_TYPE = "greyscale"
# constants for the adjustment types
BRIGHTNESS_TYPE = "brightness"
SATURATION_TYPE = "saturation"
CONTRAST_TYPE = "contrast"


def create_modifier(modifier_name, *args):
    """
    Factory function to create a modifier object,creates the modifier object
    if the arguments are valid.
    :param modifier_name: the type of modifier to create.
    :param args: arguments to pass to the modifier constructor.
    :return: the created modifier object.
    """
    # create a filter
    if modifier_name == BLUR_TYPE:
        if not check_two_positive_ints(*args):
            return None
        # convert the arguments to integers
        x, y = int(args[0]), int(args[1])
        return modifiers.Blur(x, y)
    elif modifier_name == EDGE_DETECTION_TYPE:
        return modifiers.EdgeDetection()
    elif modifier_name == SHARPEN_TYPE:
        if not check_non_negative_float(*args):
            return None
        factor = float(args[0])
        return modifiers.Sharpen(factor)
    elif modifier_name == GREY_SCALE_TYPE:
        return modifiers.GreyScale()

    # create an adjustment
    elif modifier_name == BRIGHTNESS_TYPE:
        if not check_one_float(*args):
            return None
        return modifiers.Brightness(float(args[0]))
    elif modifier_name == SATURATION_TYPE:
        if not check_non_negative_float(*args):
            return None
        return modifiers.Saturation(float(args[0]))
    elif modifier_name == CONTRAST_TYPE:
        if not check_non_negative_float(*args):
            return None
        return modifiers.Contrast(float(args[0]))


def get_modifiers_parameters():
    """
    Get the parameters for each modifier type.
    :return: a dictionary which maps modifier types with their parameters.
    """
    modifiers_parameters = {BLUR_TYPE: {"--x", "--y"},
                            EDGE_DETECTION_TYPE: {},
                            SHARPEN_TYPE: {"--factor"},
                            GREY_SCALE_TYPE: {},
                            BRIGHTNESS_TYPE: {"--factor"},
                            SATURATION_TYPE: {"--factor"},
                            CONTRAST_TYPE: {"--factor"}}
    return modifiers_parameters

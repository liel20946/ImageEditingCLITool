import filters
from utils.parameter_check import (check_two_positive_ints,
                                   check_non_negative_float)

# Constants for the filter types
BLUR_TYPE = "blur"
EDGE_DETECTION_TYPE = "edge-detection"
SHARPEN_TYPE = "sharpen"
GREY_SCALE_TYPE = "greyscale"


def create_filter(filter_name, *args):
    """
    Factory function to create a filter object,creates the filter object
    if the arguments are valid.
    :param filter_name: the type of filter to create.
    :param args: arguments to pass to the filter constructor.
    :return: the created filter object.
    """
    if filter_name == BLUR_TYPE:
        if not check_two_positive_ints(*args):
            return None
        # convert the arguments to integers
        x, y = int(args[0]), int(args[1])
        return filters.Blur(x, y)
    elif filter_name == EDGE_DETECTION_TYPE:
        return filters.EdgeDetection()
    elif filter_name == SHARPEN_TYPE:
        if not check_non_negative_float(*args):
            return None
        factor = float(args[0])
        return filters.Sharpen(factor)
    elif filter_name == GREY_SCALE_TYPE:
        return filters.GreyScale()


def get_filters_parameters():
    """
    Get the parameters for each filter type.
    :return: a dictionary which maps filter types with their parameters.
    """
    filters_parameters = {BLUR_TYPE: {"--x", "--y"},
                          EDGE_DETECTION_TYPE: {},
                          SHARPEN_TYPE: {"--factor"},
                          GREY_SCALE_TYPE: {}}
    return filters_parameters

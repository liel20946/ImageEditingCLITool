import filters

# Constants for the filter types
BOX_BLUR_TYPE = "blur"
EDGE_DETECTION_TYPE = "edge-detection"
SHARPEN_TYPE = "sharpen"
GREY_SCALE_TYPE = "greyscale"


def create_filter(filter_name, *args):
    """
    Factory function to create a filter object.
    :param filter_name: the type of filter to create.
    :param args: arguments to pass to the filter constructor.
    :return: the created filter object.
    """
    if filter_name == BOX_BLUR_TYPE:
        return filters.Blur(*args)
    elif filter_name == EDGE_DETECTION_TYPE:
        return filters.EdgeDetection()
    elif filter_name == SHARPEN_TYPE:
        return filters.Sharpen(*args)
    elif filter_name == GREY_SCALE_TYPE:
        return filters.GreyScale()
    else:
        raise ValueError("Invalid filter type")


def get_filters_parameters():
    filters_parameters = {"blur": {"--x", "--y"},
                          "edge-detection": {},
                          "sharpen": {"--factor"},
                          "greyscale": {}}
    return filters_parameters

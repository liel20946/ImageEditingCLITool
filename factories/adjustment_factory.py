import adjustments
from utils.parameter_check import check_non_negative_float, check_one_float

# Constants for the adjustment types
BRIGHTNESS_TYPE = "brightness"
SATURATION_TYPE = "saturation"
CONTRAST_TYPE = "contrast"


def create_adjustment(adjustment_type, *args):
    """
    Factory function to create an adjustment object.
    :param adjustment_type: the type of adjustment to create.
    :param args: arguments to pass to the adjustment constructor.
    :return: the created adjustment object.
    """
    if adjustment_type == BRIGHTNESS_TYPE:
        if not check_one_float(*args):
            return None
        return adjustments.Brightness(float(args[0]))
    elif adjustment_type == SATURATION_TYPE:
        if not check_non_negative_float(*args):
            return None
        return adjustments.Saturation(float(args[0]))
    elif adjustment_type == CONTRAST_TYPE:
        if not check_non_negative_float(*args):
            return None
        return adjustments.Contrast(float(args[0]))

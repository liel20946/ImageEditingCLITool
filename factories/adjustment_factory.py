import adjustments

# Constants for the adjustment types
BRIGHTNESS_TYPE = 'brightness'
SATURATION_TYPE = 'saturation'
CONTRAST_TYPE = 'contrast'


def create_adjustment(adjustment_type, *args):
    """
    Factory function to create an adjustment object.
    :param adjustment_type: the type of adjustment to create.
    :param args: arguments to pass to the adjustment constructor.
    :return: the created adjustment object.
    """
    if adjustment_type == BRIGHTNESS_TYPE:
        return adjustments.Brightness(*args)
    elif adjustment_type == SATURATION_TYPE:
        return adjustments.Saturation(*args)
    elif adjustment_type == CONTRAST_TYPE:
        return adjustments.Contrast(*args)


def get_adjustments_set():
    return {BRIGHTNESS_TYPE, SATURATION_TYPE, CONTRAST_TYPE}

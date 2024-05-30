import adjustments

BRIGHTNESS_TYPE = 'brightness'
SATURATION_TYPE = 'saturation'
CONTRAST_TYPE = 'contrast'


def create_adjustment(adjustment_type, *args):
    if adjustment_type == BRIGHTNESS_TYPE:
        return adjustments.Brightness(*args)
    elif adjustment_type == SATURATION_TYPE:
        return adjustments.Saturation(*args)
    elif adjustment_type == CONTRAST_TYPE:
        return adjustments.Contrast(*args)
    else:
        raise ValueError('Invalid adjustment type')

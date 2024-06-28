import numpy as np
from modifiers.base_modifier import BaseModifier
from utils.colors import RGB_MIN_VALUE, RGB_MAX_VALUE, RGB_MIDDLE_VALUE


class Contrast(BaseModifier):
    """
    Adjustment for changing the contrast of an image.
    """
    def __init__(self, factor):
        """
        Constructor for the Contrast class.
        :param factor: the factor to adjust the contrast by.
        """
        self.factor = factor

    def apply(self, image_array):
        """
        Adjust the contrast of an image.
        :param image_array: numpy array of the image to adjust the contrast of.
        :return: adjusted image numpy array.
        """
        adjusted_image = (RGB_MIDDLE_VALUE + self.factor *
                          (image_array.astype(np.int16) - RGB_MIDDLE_VALUE))
        return np.clip(adjusted_image, RGB_MIN_VALUE, RGB_MAX_VALUE)

import numpy as np
from adjustments.base_adjustment import BaseAdjustment
from utils.colors import RGB_MIN_VALUE, RGB_MAX_VALUE


class Contrast(BaseAdjustment):
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
        # TODO: understand how it works
        return np.clip(128 + self.factor * image_array.astype(
            np.int16) - self.factor * 128, RGB_MIN_VALUE, RGB_MAX_VALUE)

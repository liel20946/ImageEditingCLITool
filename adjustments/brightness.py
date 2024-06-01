from adjustments.base_adjustment import BaseAdjustment
import numpy as np


class Brightness(BaseAdjustment):
    """
    Adjustment for changing the brightness of an image.
    """

    def __init__(self, factor):
        """
        Constructor for the Brightness class.
        :param factor: the factor to adjust the brightness by
        """
        self.factor = factor

    def apply(self, image_array):
        """
        Adjust the brightness of an image.
        :param image_array: numpy array of the image to adjust
               the brightness of.
        :return: image_array with adjusted brightness.
        """
        adjusted_array = image_array.astype(np.int16) + self.factor
        return np.clip(adjusted_array, 0, 255)

from adjustments.base_adjustment import BaseAdjustment
from PIL import Image
import numpy as np


class Saturation(BaseAdjustment):
    """
    Adjustment for changing the saturation of an image.
    """
    def __init__(self, factor):
        """
        Constructor for the Saturation class.
        :param factor: the factor to adjust the saturation by.
        """
        self.factor = float(factor)

    def apply(self, image_array):
        """
        Adjust the saturation of an image.
        :param image_array: numpy array of the image to adjust the
               saturation of.
        :return: adjusted image numpy array.
        """
        # TODO: understand how it works
        image = Image.fromarray(image_array, 'RGB')
        hsl_image = image.convert('HSV')
        hsl_array = np.array(hsl_image)

        hsl_array[..., 1] = np.clip(hsl_array[..., 1] * self.factor, 0, 255)

        adjusted_image = Image.fromarray(hsl_array, 'HSV').convert('RGB')
        return np.array(adjusted_image)

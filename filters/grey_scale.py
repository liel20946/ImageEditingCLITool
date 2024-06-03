from filters.base_filter import BaseFilter
from utils.colors import (GREYSCALE_SHAPE_LENGTH, RGB_SHAPE_LENGTH, RED_WEIGHT,
                          GREEN_WEIGHT, BLUE_WEIGHT)
import numpy as np


class GreyScale(BaseFilter):
    """
    Filter for converting an image to greyscale.
    """

    def apply(self, image_array):
        """
        Convert an image to greyscale.
        :param image_array: numpy array of the image to convert to greyscale.
        :return: numpy array of the greyscale image.
        """
        if len(image_array.shape) == GREYSCALE_SHAPE_LENGTH:
            return image_array
        return np.dot(image_array[..., :RGB_SHAPE_LENGTH],
                      [RED_WEIGHT, GREEN_WEIGHT, BLUE_WEIGHT])

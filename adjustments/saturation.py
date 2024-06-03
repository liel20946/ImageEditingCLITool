from adjustments.base_adjustment import BaseAdjustment
from utils.colors import (RGB_SHAPE_LENGTH, RGBA_CHANNEL_SIZE,
                          CHANNEL_SIZE_INDEX, RGB_MIN_VALUE, RGB_MAX_VALUE)
import numpy as np
import utils.colors as cs


class Saturation(BaseAdjustment):
    """
    Adjustment for changing the saturation of an image.
    """
    def __init__(self, factor):
        """
        Constructor for the Saturation class.
        :param factor: the factor to adjust the saturation by.
        """
        self.factor = factor

    def apply(self, image_array):
        """
        Adjust the saturation of an image.
        :param image_array: numpy array of the image to adjust the
               saturation of.
        :return: adjusted image numpy array.
        """
        if len(image_array.shape) != RGB_SHAPE_LENGTH:
            return image_array
        is_rgba = image_array.shape[CHANNEL_SIZE_INDEX] == RGBA_CHANNEL_SIZE

        rgb_image = image_array[..., :RGB_SHAPE_LENGTH]
        a_channel = image_array[..., RGB_SHAPE_LENGTH:] if is_rgba else None

        hsv_array = cs.rgb_to_hsv(rgb_image)

        hsv_array[..., 1] = np.clip(hsv_array[..., 1] * self.factor,
                                    RGB_MIN_VALUE, RGB_MAX_VALUE)

        adjusted_image = cs.hsv_to_rgb(hsv_array)
        adjusted_image = np.clip(adjusted_image, RGB_MIN_VALUE, RGB_MAX_VALUE)

        if is_rgba:
            adjusted_image_with_alpha = np.dstack(
                [np.array(adjusted_image), a_channel])
            return adjusted_image_with_alpha
        return np.array(adjusted_image)

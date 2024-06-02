from adjustments.base_adjustment import BaseAdjustment
from PIL import Image
import numpy as np
import utils.color_space as cs

# Constants
RGB_SHAPE_LENGTH = 3
RGBA_CHANNEL_SIZE = 4


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
        if len(image_array.shape) != RGB_SHAPE_LENGTH:
            return image_array
        is_rgba = image_array.shape[2] == RGBA_CHANNEL_SIZE

        # Extract RGB channels and alpha channel (if present)
        rgb_image = image_array[..., :RGB_SHAPE_LENGTH]
        alpha_channel = image_array[..., RGB_SHAPE_LENGTH:] if is_rgba else None

        # Convert the RGB image to HSV
        hsv_array = cs.rgb_to_hsv(rgb_image)

        # Adjust the saturation channel
        hsv_array[..., 1] = np.clip(hsv_array[..., 1] * self.factor, 0, 255)

        adjusted_image = cs.hsv_to_rgb(hsv_array)
        adjusted_image = np.clip(adjusted_image, 0, 255)

        if is_rgba:
            # Combine the adjusted RGB image with the alpha channel
            adjusted_image_with_alpha = np.dstack(
                [np.array(adjusted_image), alpha_channel])
            return adjusted_image_with_alpha
        return np.array(adjusted_image)

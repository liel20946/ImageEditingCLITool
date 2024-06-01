from adjustments.base_adjustment import BaseAdjustment
from PIL import Image
import numpy as np

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
        # Convert the RGB image to PIL image
        image = Image.fromarray(rgb_image, 'RGB')

        # Convert the RGB image to HSV
        hsl_image = image.convert('HSV')
        hsl_array = np.array(hsl_image)

        # Adjust the saturation channel
        hsl_array[..., 1] = np.clip(hsl_array[..., 1] * self.factor, 0, 255)
        # Convert the adjusted HSV image back to RGB
        adjusted_image = Image.fromarray(hsl_array, 'HSV').convert('RGB')

        if is_rgba:
            # Combine the adjusted RGB image with the alpha channel
            adjusted_image_with_alpha = np.dstack(
                [np.array(adjusted_image), alpha_channel])
            return adjusted_image_with_alpha
        return np.array(adjusted_image)

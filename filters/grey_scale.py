from filters.base_filter import BaseFilter
import numpy as np

# weights for RGB to greyscale conversion
RED_WEIGHT = 0.2989
GREEN_WEIGHT = 0.5870
BLUE_WEIGHT = 0.1140


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
        if len(image_array.shape) == 2: # in case the image is already greyscale
            return image_array
        return np.dot(image_array[..., :3],
                      [RED_WEIGHT, GREEN_WEIGHT, BLUE_WEIGHT])


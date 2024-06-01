import numpy as np

from filters.base_filter import BaseFilter
import factories.filter_factory as filter_factory

# Constants
RGB_SHAPE_LENGTH = 3


class Sharpen(BaseFilter):
    """
    Filter for sharpening an image.
    """

    def __init__(self, factor):
        """
        Constructor for the Sharpen class.
        :param factor:
        """
        self.factor = factor
        self.edge_detection = filter_factory.create_filter('edge-detection')

    def apply(self, image_array):
        """
        Apply the sharpen filter to an image, using edge detection.
        :param image_array:
        :return:
        """
        # TODO: understand how this works
        edges = self.edge_detection.apply(image_array)
        if len(image_array.shape) == RGB_SHAPE_LENGTH:
            edges = edges[:, :, None].repeat(image_array.shape[2], axis=2)
        sharpened = image_array.astype(np.int16) + self.factor * edges
        return np.clip(sharpened, 0, 255)

import numpy as np

from filters.base_filter import BaseFilter
from filters.edge_detection import EdgeDetection


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
        self.edge_detection = EdgeDetection()

    def apply(self, image_array):
        """
        Apply the sharpen filter to an image, using edge detection.
        :param image_array:
        :return:
        """
        # TODO: understand how this works
        edges = self.edge_detection.apply(image_array)
        edges = edges[:, :, None].repeat(3, axis=2)
        sharpened = image_array.astype(np.int16) + self.factor * edges
        return np.uint8(np.clip(sharpened, 0, 255))

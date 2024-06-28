import numpy as np

from modifiers.base_modifier import BaseModifier
import factories.modifier_factory as filter_factory
from utils.convolution import convolve_2d
from utils.colors import RGB_MAX_VALUE


class EdgeDetection(BaseModifier):
    """
    Filter for applying edge detection to an image.
    """
    def __init__(self):
        """
        Constructor for the EdgeDetection class.
        """
        # using sobel operator
        self.vertical_kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        self.horizontal_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        self.grey_scale_filter = filter_factory.create_modifier("greyscale")

    def apply(self, image_array):
        """
        Apply the edge detection filter to an image, using sobel operator.
        :param image_array: numpy array of the image to apply the filter to.
        :return: image_array with the edge detection filter applied.
        """
        greyed_image = self.grey_scale_filter.apply(image_array)

        vertical_edges = convolve_2d(greyed_image, self.vertical_kernel)
        horizontal_edges = convolve_2d(greyed_image, self.horizontal_kernel)

        edges = np.sqrt(np.square(vertical_edges) +
                        np.square(horizontal_edges))
        # normalize the edges to increase visibility
        edges = (edges / np.max(edges)) * RGB_MAX_VALUE
        return edges

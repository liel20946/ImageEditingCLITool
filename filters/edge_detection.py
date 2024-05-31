import numpy as np

from filters.base_filter import BaseFilter
from filters.grey_scale import GreyScale
from utils.convolution import convolve_2d


class EdgeDetection(BaseFilter):
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

    def apply(self, image_array):
        """
        Apply the edge detection filter to an image.
        :param image_array: numpy array of the image to apply the filter to.
        :return: image_array with the edge detection filter applied.
        """
        grey_scale_filter = GreyScale()
        greyed_image = grey_scale_filter.apply(image_array)

        vertical_edges = convolve_2d(greyed_image, self.vertical_kernel)
        horizontal_edges = convolve_2d(greyed_image, self.horizontal_kernel)

        edges = np.sqrt(np.square(vertical_edges) + np.square(horizontal_edges))
        edges = (edges / np.max(edges)) * 255

        return np.uint8(edges)

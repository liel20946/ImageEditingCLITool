from filters.base_filter import BaseFilter
from utils.convolution import convolve_md
import numpy as np


class BoxBlur(BaseFilter):
    """
    Filter for applying a box blur to an image.
    """
    def __init__(self, x, y):
        """
        Constructor for the BoxBlur class.
        :param x: x dimension of the kernel matrix.
        :param y: y dimension of the kernel matrix.
        """
        self.x = x
        self.y = y
        # initialize the kernel matrix, normalized 1's matrix
        self.kernel = np.full((x, y), 1 / (x * y))

    def apply(self, image_array):
        """
        Apply the box blur filter to an image.
        :param image_array: numpy array of the image to apply the filter to.
        :return: image_array with the box blur filter applied.
        """
        return convolve_md(image_array, self.kernel)

from modifiers.base_modifier import BaseModifier
from utils.convolution import convolve
import numpy as np


class Blur(BaseModifier):
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
        self.kernel = np.full((self.x, self.y), 1 / (self.x * self.y))

    def apply(self, image_array):
        """
        Apply the box blur filter to an image.
        :param image_array: numpy array of the image to apply the filter to.
        :return: image_array with the box blur filter applied.
        """
        return convolve(image_array, self.kernel)

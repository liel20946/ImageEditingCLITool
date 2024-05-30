import numpy as np

from filters.base_filter import BaseFilter
from filters.grey_scale import GreyScale
from utils.convolution import convolve_2d


class EdgeDetection(BaseFilter):
    def __init__(self):
        # using sobel operator
        self.vertical_kernel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        self.horizontal_kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    def apply(self, image_array):
        # convert image to grayscale
        grey_scale_filter = GreyScale()
        greyed_image = grey_scale_filter.apply(image_array)
        vertical_edges = convolve_2d(greyed_image, self.vertical_kernel)
        horizontal_edges = convolve_2d(greyed_image, self.horizontal_kernel)
        return np.uint8(np.sqrt(vertical_edges ** 2 + horizontal_edges ** 2))

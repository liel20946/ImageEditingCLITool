from filters.base_filter import BaseFilter
from utils.convolution import convolve_md
import numpy as np


class BoxBlur(BaseFilter):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # initialize the kernel matrix, normalized 1's matrix
        self.kernel = np.full((x, y), 1 / (x * y))

    def apply(self, image_array):
        return convolve_md(image_array, self.kernel)

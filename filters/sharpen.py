import numpy as np

from filters.base_filter import BaseFilter
from filters.edge_detection import EdgeDetection


class Sharpen(BaseFilter):
    def __init__(self, factor):
        self.factor = factor
        self.edge_detection = EdgeDetection()

    def apply(self, image_array):
        edges = self.edge_detection.apply(image_array)
        # convert edges from shape (x, y) to shape (x, y, 3)
        edges = edges[:, :, None].repeat(3, axis=2)
        return np.uint8(image_array + self.factor * edges)

import numpy as np

from filters.base_filter import BaseFilter
from filters.edge_detection import EdgeDetection


class Sharpen(BaseFilter):
    def __init__(self, factor):
        self.factor = factor
        self.edge_detection = EdgeDetection()

    def apply(self, image_array):
        # TODO: understand how this works
        edges = self.edge_detection.apply(image_array)
        # convert edges from shape (x, y) to shape (x, y, 3)
        edges = edges[:, :, None].repeat(3, axis=2)
        sharpened = image_array.astype(np.int16) + self.factor * edges

        return np.uint8(np.clip(sharpened, 0, 255))

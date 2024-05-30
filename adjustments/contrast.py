from adjustments.base_adjustment import BaseAdjustment
import numpy as np


class Contrast(BaseAdjustment):
    def __init__(self, factor):
        self.factor = factor

    def apply(self, image_array):
        # Apply contrast adjustment
        # TODO: understand how it works
        return np.uint8(np.clip(128 + self.factor * image_array.astype(
            np.int16) - self.factor * 128, 0, 255))

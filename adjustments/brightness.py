from adjustments.base_adjustment import BaseAdjustment
import numpy as np


class Brightness(BaseAdjustment):
    def __init__(self, factor):
        self.factor = factor

    def apply(self, image_array):
        # Apply contrast adjustment
        adjusted_array = image_array.astype(np.int16) + self.factor
        # Clip pixel values to 0-255, and convert to uint8
        return np.uint8(np.clip(adjusted_array, 0, 255))

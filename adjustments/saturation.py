from adjustments.base_adjustment import BaseAdjustment
from PIL import Image
import numpy as np


class Saturation(BaseAdjustment):
    def __init__(self, factor):
        self.factor = float(factor)

    def apply(self, image_array):
        # TODO: understand how it works
        # Convert the image array from RGB to HSL
        image = Image.fromarray(image_array, 'RGB')
        hsl_image = image.convert('HSV')
        hsl_array = np.array(hsl_image)

        # Adjust the saturation
        hsl_array[..., 1] = np.clip(hsl_array[..., 1] * self.factor, 0, 255)

        # Convert back to RGB
        adjusted_image = Image.fromarray(hsl_array, 'HSV').convert('RGB')
        return np.array(adjusted_image)

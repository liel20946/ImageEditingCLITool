import numpy as np

from modifiers.base_modifier import BaseModifier
from utils.colors import RGB_SHAPE_LENGTH, RGB_MIN_VALUE, RGB_MAX_VALUE, \
    CHANNEL_SIZE_INDEX
import factories.modifier_factory as filter_factory


class Sharpen(BaseModifier):
    """
    Filter for sharpening an image.
    """

    def __init__(self, factor):
        """
        Constructor for the Sharpen class.
        :param factor:
        """
        self.factor = factor
        self.edge_detection = filter_factory.create_modifier('edge-detection')

    def apply(self, image_array):
        """
        Apply the sharpen filter to an image, using edge detection.
        :param image_array:
        :return:
        """
        edges = self.edge_detection.apply(image_array)
        if len(image_array.shape) == RGB_SHAPE_LENGTH:
            num_channels = image_array.shape[CHANNEL_SIZE_INDEX]
            edges = edges[:, :, None].repeat(num_channels, axis=2)
        sharpened = image_array.astype(np.int16) + self.factor * edges
        return np.clip(sharpened, RGB_MIN_VALUE, RGB_MAX_VALUE)

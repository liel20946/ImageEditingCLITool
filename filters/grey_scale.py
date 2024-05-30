from filters.base_filter import BaseFilter
import numpy as np

RED_WEIGHT = 0.2989
GREEN_WEIGHT = 0.5870
BLUE_WEIGHT = 0.1140


class GreyScale(BaseFilter):
    def apply(self, image_array):
        return np.dot(image_array[..., :3],
                      [RED_WEIGHT, GREEN_WEIGHT, BLUE_WEIGHT])

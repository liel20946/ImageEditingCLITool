from abc import ABC, abstractmethod


class BaseAdjustment(ABC):
    """
    Base class for image adjustments.
    """
    @abstractmethod
    def apply(self, image_array):
        """
        Apply the adjustment to the image.
        :param image_array: image numpy array to adjust.
        :return: adjust image numpy array.
        """
        pass

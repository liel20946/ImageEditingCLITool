from abc import ABC, abstractmethod


class BaseFilter(ABC):
    """
    Base class for image filters.
    """
    @abstractmethod
    def apply(self, image_array):
        """
        Apply the filter to the image.
        :param image_array: image numpy array to apply the filter to.
        :return: filtered image numpy array.
        """
        pass

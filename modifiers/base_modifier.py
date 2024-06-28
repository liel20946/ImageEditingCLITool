from abc import ABC, abstractmethod


class BaseModifier(ABC):
    """
    Base class for image modifiers.
    """
    @abstractmethod
    def apply(self, image_array):
        """
        Apply the modifier to the image.
        :param image_array: image numpy array to apply the modifier to.
        :return: modified image numpy array.
        """
        pass

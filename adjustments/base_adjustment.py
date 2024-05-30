from abc import ABC, abstractmethod


class BaseAdjustment(ABC):
    @abstractmethod
    def apply(self, image_array):
        pass

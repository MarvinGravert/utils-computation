import numpy as np
from abc import ABC, abstractmethod


class BaseAlgorithm(ABC):

    @abstractmethod
    def register_points(self,
                        points_set_1: np.ndarray,
                        points_set_2: np.ndarray
                        ) -> np.ndarray:
        pass

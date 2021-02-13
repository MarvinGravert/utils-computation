import numpy as np
from abc import ABC, abstractmethod
from typing import Tuple


class BaseAlgorithm(ABC):
    def check_adjust_dimension(self, point_set: np.ndarray
                               ) -> np.ndarray:
        # check data transmitted in column matrix or in row matrix and transform
        # into column matrix
        row, column = point_set.shape
        if row == 3 and column >= 3:
            # column matrix
            return point_set
        elif row >= 3 and column == 3:
            # row matrix
            return point_set.T
        else:
            raise Exception("Data matrix not correct format")
    @abstractmethod
    def register_points(self,
                        points_set_1: np.ndarray,
                        points_set_2: np.ndarray
                        ) -> Tuple[np.ndarray, np.ndarray]:
        raise NotImplementedError

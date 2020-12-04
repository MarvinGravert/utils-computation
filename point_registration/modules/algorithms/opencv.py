"""
Find Transformation from Point Set 1 to Point Set 1 using Kabsch algorithm
"""
from modules.base_compute import BaseAlgorithm
import numpy as np
import cv2
import logging
from typing import Tuple

from config.config import RANSAC_CONFIDENCE, RANSAC_THRESHOLD


class OpencvAlgorithm(BaseAlgorithm):
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

    def register_points(self, point_set_1: np.ndarray,
                        point_set_2: np.ndarray
                        ) -> Tuple[np.ndarray, np.ndarray]:
        """Find optimal affine transformation between the points sets 


                function used: 
                https://docs.opencv.org/4.0.0/d9/d0c/group__calib3d.html#ga396afb6411b30770e56ab69548724715
        Args:
            point_set_1 (np.ndarray): 3xn 
            point_set_2 (np.ndarray): 3xn

        Returns:
            np.ndarray: returns R (3x3 rot matrix), t (3x1 matrix)
        """
        # Input: expects 3xN matrix of points
        # Returns R,t
        # R = 3x3 rotation matrix
        # t = 3x1 column vector

        A = self.check_adjust_dimension(point_set_1)
        B = self.check_adjust_dimension(point_set_2)
        A = A.T
        B = B.T
        retval, out, inlier = cv2.estimateAffine3D(src=A,
                                                   dst=B,
                                                   ransacThreshold=RANSAC_THRESHOLD,
                                                   confidence=RANSAC_CONFIDENCE,
                                                   )
        return out[:, :3], out[:, 3]

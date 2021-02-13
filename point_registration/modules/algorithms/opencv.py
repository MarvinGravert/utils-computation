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
        logging.debug(f"\n {A}")
        B = B.T
        logging.debug(f"\n {B}")
        retval, out, inlier = cv2.estimateAffine3D(src=A,
                                                   dst=B,
                                                   ransacThreshold=RANSAC_THRESHOLD,
                                                   confidence=RANSAC_CONFIDENCE,
                                                   )
        logging.info(f"Number of point correspondances: {A.shape[0]}")
        logging.info(
            f"Number of inlier: {sum([1 if x == 1 else 0 for x in inlier])}")

        logging.info(f"""
            Parameters used for ransac:
            Threshold {RANSAC_THRESHOLD}
            CONFIDENCE {RANSAC_CONFIDENCE}
        """)
        logging.info(f"Result: \n {out}")

        return out[:, :3], out[:, 3]

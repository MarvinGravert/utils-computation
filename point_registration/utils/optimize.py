"""Optimize the Transformation using non linear optimization
Point set A and point set B shoudl be provided to this function as well
as the matrix R and vector t 

The relation should be B_i=R@A_i+t aka A->B

The called module will return a R*,t* optimized regarding some nonlinear
optimization algorithm

For the moment it is assumed to be an unbounded problem.
"""

import numpy as np

from scipy.optimize import least_squares
"""
The problem we are trying to solve is argmin (sum_i->m[(B_i- F(A_i,X))²])
see: https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm

To do this we use the least_squares solver from scipy:
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html

We need to provide a function and initial values.
The function should be F(X, *args,**kwargs)->residulas
In our case X is the flattened R and t and the residual are the differences 
B_i-R@A_i+t across all N point correspondances i=1,2,...,N

Hence, X is a (9+3)x1 vector and residual is a Nx1 vector

So in our case 
"""
class ObjectiveFunction():
    def __init__(self,point_set_1:np.ndarray,point_set_2:np.ndarray):
        self._point_set_1=point_set_1
        self._point_set_2=point_set_2
    def calc_residuals(self,X:np.ndarray)->np.ndarray:
        """Calculates the resuldials across the point correspondances


        Args:
            X (np.ndarray): 12x1 vector containing row major flattend R and t e.g [r11,r12,r13,r21,...,t1,t2,t3]

        Returns:
            np.ndarray: Nx1 vectors containing the residuals 
        """
        residuals=[]
        R=X[0:9].reshape([3,3])
        t=X[9:].reshape([3,1])
        for vec_A, vec_B in zip(self._point_set_1,self._point_set_2):
            # print(vec_A.reshape([3,1]))
            # print(vec_B.reshape([3,1]))
            vec_A_in_B=R@vec_A.reshape([3,1])+t
            # print(vec_A_in_B)
            residuals.append(np.linalg.norm(vec_B-vec_A_in_B))
        return np.array(residuals)
def find_optimal_transformation(point_set_1,point_set_2, R:np.ndarray, t:np.ndarray):
    costfunc=ObjectiveFunction(point_set_1=point_set_1,point_set_2=point_set_2)

    x_0=np.vstack([R,t.flatten()]).flatten()
    res=least_squares(costfunc.calc_residuals, x_0)
    # print(res)
    return res.x[0:9].reshape([3,3]), res.x[9:].reshape([3,1])


if __name__=="__main__":
    pass

from typing import Tuple

import numpy as np
from loguru import logger

from config.config import RANSAC_THRESHOLD, RANSAC_CONFIDENCE

from utils.check_cost_function import check_cost_function
from client import run_with_config
        
from modules.optimization import optimize

def show_Matrix(R, t):
    # logger.info(f"""
    # Rotationmatrix:
    # {R[0,:]}
    # {R[1,:]}
    # {R[2,:]}
    # Translationvektor:
    # {t[0]}
    # {t[1]}
    # {t[2]}
    # """)
    print(np.hstack([R,t]))
    from scipy.spatial.transform import Rotation
    R = Rotation.from_matrix(R)
    # logger.info(f"\n {R.as_matrix()}")
    

def get_data_nadine(filename="Corresparray.txt"):
    import csv
    with open(filename, 'r') as f:
        first = [x for x in csv.reader(f, delimiter=',')]
    # return len(first), len(second)
    # t = np.loadtxt(filename, skiprows=1, delimiter=",")
    p = first[1:4]
    q = first[4:]
    p = np.array(p).T
    q = np.array(q).T
    return (np.asfarray(p[:-1]), np.asfarray(q[:-1]))


algorithm_dict={
        "type": "OPENCV",
        "optimize": False, #boolean, False
        "ransac": [0.15, 0.8] #[threshold, confidence]list of floats 
    }

if __name__ == "__main__":
    logger.info("Starting Comparison")
    """
    IMPORT DATA
    """
    point_set_1, point_set_2 = get_data_nadine()
    ## data from her 3D experiments
    R_nadine=np.array([[0.998815,-0.001533,0.010493],
                [0.020139,1.014782,-0.003107],
                [0.044471,0.009391, 1.001996 ]])           
    t_nadine=np.array([0.001209,0.017572,0.066353]).reshape([3, 1])
    """
    RUN point registration
    """
    R,t=run_with_config(point_set_1,point_set_2,algorithm_dict)
    """
    Compare results
    """
    temp=check_cost_function(point_set_1,point_set_2, R,t)
    print(f"Pre optimisation Results: {temp}")
    temp=check_cost_function(point_set_2,point_set_1, R_nadine,t_nadine)
    print(f"Nadine: {temp}")
    opt=optimize.Optimizer(point_set_1,point_set_2,R,t)
    R_opt,t_opt=opt.find_optimal_rotation()
    temp=check_cost_function(point_set_1,point_set_2, R_opt,t_opt)
    print(f"Optimisation no correction: {temp}")
    R_cor=opt.correct_rotation_matrix(R_opt)
    temp=check_cost_function(point_set_1,point_set_2, R_cor,t_opt)
    print(f"Optimisation with correction: {temp}")
    show_Matrix(R_cor,t)
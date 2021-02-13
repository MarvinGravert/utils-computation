
import point_registration_pb2
import point_registration_pb2_grpc
import grpc
import numpy as np

import logging
from typing import Tuple

from config.config import GRPC_PORT, RUNTIME_HOST
from config.config import RANSAC_THRESHOLD, RANSAC_CONFIDENCE

from utils.check_cost_function import check_results
def run():
    with grpc.insecure_channel(f"{RUNTIME_HOST}:{GRPC_PORT}") as channel:
        stub = point_registration_pb2_grpc.PointRegisteringStub(channel)
        logging.info(f"Connecting to {RUNTIME_HOST}:{GRPC_PORT}")
        # TODO: Implement algorithm type via api_types and env variable
        algorithm = "opencv"  # opencv,kabsch
        point_set_1, point_set_2 = get_data_nadine()

        point_set_1 = [point_registration_pb2.vector(
            vector_data=x) for x in point_set_1]
        point_set_2 = [point_registration_pb2.vector(
            vector_data=x) for x in point_set_2]
        objToSend = point_registration_pb2.input(
            algorithm=algorithm,
            point_set_1=point_set_1,
            point_set_2=point_set_2,
        )
        response = stub.registerPoints(objToSend)
        R = list()
        t = list()
        for row, entry in zip(response.rotation_matrix,
                              response.translation_vector.vector_data):
            R.append(row.row)
            t.append(entry)
        R = np.array(R)
        t = np.array(t).reshape([3, 1])
        # present_result(R, t)
        
        point_set_1, point_set_2 = get_data_nadine()
        Rnad=np.array([[0.998815,-0.001533,0.010493],
                    [0.020139,1.014782,-0.003107],
                    [0.044471,0.009391, 1.001996 ]])           
        tnad=np.array([0.001209,0.017572,0.066353]).reshape([3, 1])
      
        temp=check_results(point_set_1=point_set_1,point_set_2=point_set_2, R=R,t=t)
        print(temp)
        temp=check_results(point_set_1=point_set_2,point_set_2=point_set_1, R=Rnad,t=tnad)
        print(temp)
        from utils.optimize import find_optimal_transformation
        R,t=find_optimal_transformation(point_set_1=point_set_1,point_set_2=point_set_2, R=R,t=t)
        temp=check_results(point_set_1=point_set_1,point_set_2=point_set_2, R=R,t=t)
        print(temp)
        present_result(R,t)
        u,sig,v=np.linalg.svd(R)
        u[:,2]=-u[:,2]
        print(u@v)
        print(np.linalg.det(u@v))
        temp=check_results(point_set_1=point_set_1,point_set_2=point_set_2, R=R,t=t)
        print(temp)

def present_result(rot, vec):
    logging.info(f"""
    Rotationmatrix:
    {rot[0,:]}
    {rot[1,:]}
    {rot[2,:]}
    Translationvektor:
    {vec[0]}
    {vec[1]}
    {vec[2]}
    """)
    from scipy.spatial.transform import Rotation
    R = Rotation.from_matrix(rot)
    logging.info(f"\n {R.as_matrix()}")
    

def get_data_from_file(filename_1="point_set_1.txt",
                       filename_2="point_set_2.txt"
                       ) -> Tuple[np.ndarray, np.ndarray]:
    return np.loadtxt(filename_1), np.loadtxt(filename_2)


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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()
    # ret = get_data_nadine()
    # print(ret)

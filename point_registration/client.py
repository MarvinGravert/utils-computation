import point_registration_pb2
import point_registration_pb2_grpc
import grpc
import numpy as np

import logging
from typing import Tuple

from config.config import GRPC_PORT, RUNTIME_HOST


def run():
    with grpc.insecure_channel(f"{RUNTIME_HOST}:{GRPC_PORT}") as channel:
        stub = point_registration_pb2_grpc.PointRegisteringStub(channel)
        logging.info(f"Connecting to {RUNTIME_HOST}:{GRPC_PORT}")
        # TODO: Implement algorithm type via api_types and env variable
        algorithm = "kabsch"  # opencv
        point_set_1, point_set_2 = get_data_from_file()

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


def get_data_from_file(filename_1="point_set_1.txt",
                       filename_2="point_set_2.txt"
                       ) -> Tuple[np.ndarray, np.ndarray]:
    return np.loadtxt(filename_1), np.loadtxt(filename_2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()

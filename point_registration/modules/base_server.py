from typing import Tuple
import numpy as np
import point_registration_pb2
import point_registration_pb2_grpc
from modules.algorithms.kabsch import KabschAlgorithm
from modules.algorithms.opencv import OpencvAlgorithm
from typing import Tuple
import grpc


class PointRegistering(point_registration_pb2_grpc.PointRegisteringServicer):
    def registerPoints(self, request, context):
        point_set_1, point_set_2 = self.prepare_data(request)
        if request.algorithm == "kabsch":
            # TODO: use api.types to implement these as enumns rather than string
            R, t = KabschAlgorithm().register_points(point_set_1, point_set_2)
        if request.algorithm == "opencv":
            R, t = OpencvAlgorithm().register_points(point_set_1, point_set_2)

        response = point_registration_pb2.output(
            rotation_matrix=[point_registration_pb2.matrix_row(row=x)
                             for x in np.ndarray.tolist(R)],
            translation_vector=point_registration_pb2.vector(
                vector_data=t)
        )
        return response

    def prepare_data(self, request) -> Tuple[np.ndarray, np.ndarray]:
        point_set_1 = list()
        point_set_2 = list()
        for x in request.point_set_1:
            point_set_1.append(np.array(x.vector_data))
        point_set_2 = [np.array(x.vector_data) for x in request.point_set_2]
        return np.array(point_set_1), np.array(point_set_2)

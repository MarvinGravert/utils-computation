import point_registration_pb2
import point_registration_pb2_grpc
import logging

from config.config import GRPC_PORT, RUNTIME_HOST
import grpc


def run():
    with grpc.insecure_channel(f"{RUNTIME_HOST}:{GRPC_PORT}") as channel:
        stub = point_registration_pb2_grpc.PointRegisteringStub(channel)
        # TODO: implement with api types
        algorithm = "kabsch"
        points_1 = [[1, 2, 3], [3, 2, 3], [4, 3, 2], [4, 6, 7]]

        points_2 = [[1, 2, 3], [3, 2, 3], [4, 3, 2], [4, 6, 7]]
        point_set_1 = [point_registration_pb2.vector(
            vector_data=x) for x in points_1]
        point_set_2 = [point_registration_pb2.vector(
            vector_data=x) for x in points_2]
        objToSend = point_registration_pb2.input(
            algorithm=algorithm,
            point_set_1=point_set_1,
            point_set_2=point_set_2,
        )
        response = stub.registerPoints(objToSend)
        for x in response.rotation_matrix:
            print(x)
        print(response.translation_vector)
        # if not with=>channel.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run()

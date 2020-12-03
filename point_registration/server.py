import point_registration_pb2
import point_registration_pb2_grpc
from config.config import GRPC_PORT, RUNTIME_HOST
from concurrent import futures
import logging
import grpc

from modules.base_server import PointRegistering


def serve():
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=2))
    point_registration_pb2_grpc.add_PointRegisteringServicer_to_server(
        servicer=PointRegistering(), server=server)
    server.add_insecure_port(f"[::]:{GRPC_PORT}")
    server.start()
    server.wait_for_termination()


class Server:
    def serve(self):
        logging.info(
            f"Server started on Address: [::], Port: {GRPC_PORT}")
        serve()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    Server().serve()

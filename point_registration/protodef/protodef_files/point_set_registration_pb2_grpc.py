# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import point_set_registration_pb2 as point__set__registration__pb2


class PointSetRegisteringStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerPointSet = channel.unary_unary(
                '/PointSetRegistering/registerPointSet',
                request_serializer=point__set__registration__pb2.Input.SerializeToString,
                response_deserializer=point__set__registration__pb2.Output.FromString,
                )


class PointSetRegisteringServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registerPointSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PointSetRegisteringServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registerPointSet': grpc.unary_unary_rpc_method_handler(
                    servicer.registerPointSet,
                    request_deserializer=point__set__registration__pb2.Input.FromString,
                    response_serializer=point__set__registration__pb2.Output.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PointSetRegistering', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PointSetRegistering(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registerPointSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PointSetRegistering/registerPointSet',
            point__set__registration__pb2.Input.SerializeToString,
            point__set__registration__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

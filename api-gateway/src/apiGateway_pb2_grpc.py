# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import apiGateway_pb2 as apiGateway__pb2


class ApiGatewayServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadFile = channel.unary_unary(
                '/ApiGatewayService/ReadFile',
                request_serializer=apiGateway__pb2.ReadFileRequestData.SerializeToString,
                response_deserializer=apiGateway__pb2.ReadFileResponseData.FromString,
                )


class ApiGatewayServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApiGatewayServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFile,
                    request_deserializer=apiGateway__pb2.ReadFileRequestData.FromString,
                    response_serializer=apiGateway__pb2.ReadFileResponseData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ApiGatewayService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ApiGatewayService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ApiGatewayService/ReadFile',
            apiGateway__pb2.ReadFileRequestData.SerializeToString,
            apiGateway__pb2.ReadFileResponseData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
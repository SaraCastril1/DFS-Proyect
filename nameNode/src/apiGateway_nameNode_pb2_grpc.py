# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import apiGateway_nameNode_pb2 as apiGateway__nameNode__pb2


class NameNodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WriteFile = channel.unary_unary(
                '/NameNodeService/WriteFile',
                request_serializer=apiGateway__nameNode__pb2.WriteFileRequest.SerializeToString,
                response_deserializer=apiGateway__nameNode__pb2.WriteFileResponse.FromString,
                )
        self.ReadFile = channel.unary_unary(
                '/NameNodeService/ReadFile',
                request_serializer=apiGateway__nameNode__pb2.ReadFileRequest.SerializeToString,
                response_deserializer=apiGateway__nameNode__pb2.ReadFileResponse.FromString,
                )
        self.ListFiles = channel.unary_unary(
                '/NameNodeService/ListFiles',
                request_serializer=apiGateway__nameNode__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=apiGateway__nameNode__pb2.ListFilesResponse.FromString,
                )
        self.AddFile = channel.unary_unary(
                '/NameNodeService/AddFile',
                request_serializer=apiGateway__nameNode__pb2.AddFileRequest.SerializeToString,
                response_deserializer=apiGateway__nameNode__pb2.AddFileResponse.FromString,
                )


class NameNodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WriteFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddFile(self, request, context):
        """rpc DeleteFile(DeleteFilesRequest) returns (DeleteFilesResponse);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameNodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WriteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteFile,
                    request_deserializer=apiGateway__nameNode__pb2.WriteFileRequest.FromString,
                    response_serializer=apiGateway__nameNode__pb2.WriteFileResponse.SerializeToString,
            ),
            'ReadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadFile,
                    request_deserializer=apiGateway__nameNode__pb2.ReadFileRequest.FromString,
                    response_serializer=apiGateway__nameNode__pb2.ReadFileResponse.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=apiGateway__nameNode__pb2.ListFilesRequest.FromString,
                    response_serializer=apiGateway__nameNode__pb2.ListFilesResponse.SerializeToString,
            ),
            'AddFile': grpc.unary_unary_rpc_method_handler(
                    servicer.AddFile,
                    request_deserializer=apiGateway__nameNode__pb2.AddFileRequest.FromString,
                    response_serializer=apiGateway__nameNode__pb2.AddFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameNodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameNodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WriteFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/WriteFile',
            apiGateway__nameNode__pb2.WriteFileRequest.SerializeToString,
            apiGateway__nameNode__pb2.WriteFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/ReadFile',
            apiGateway__nameNode__pb2.ReadFileRequest.SerializeToString,
            apiGateway__nameNode__pb2.ReadFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/ListFiles',
            apiGateway__nameNode__pb2.ListFilesRequest.SerializeToString,
            apiGateway__nameNode__pb2.ListFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/AddFile',
            apiGateway__nameNode__pb2.AddFileRequest.SerializeToString,
            apiGateway__nameNode__pb2.AddFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
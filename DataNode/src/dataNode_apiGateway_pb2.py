# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataNode-apiGateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64\x61taNode-apiGateway.proto\x1a\x1egoogle/protobuf/wrappers.proto\"h\n\x14WriteFileRequestData\x12\x0e\n\x06\x66older\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12.\n\tfile_data\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.BytesValue\"E\n\x15WriteFileResponseData\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\t\x12\x1b\n\x13\x64\x61ta_node_addresses\x18\x02 \x03(\t\"(\n\x13ReadFileRequestData\x12\x11\n\tfile_name\x18\x01 \x01(\t\"F\n\x14ReadFileResponseData\x12.\n\tfile_data\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValue2\x86\x01\n\x0f\x44\x61taNodeService\x12:\n\tWriteFile\x12\x15.WriteFileRequestData\x1a\x16.WriteFileResponseData\x12\x37\n\x08ReadFile\x12\x14.ReadFileRequestData\x1a\x15.ReadFileResponseDatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dataNode_apiGateway_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_WRITEFILEREQUESTDATA']._serialized_start=61
  _globals['_WRITEFILEREQUESTDATA']._serialized_end=165
  _globals['_WRITEFILERESPONSEDATA']._serialized_start=167
  _globals['_WRITEFILERESPONSEDATA']._serialized_end=236
  _globals['_READFILEREQUESTDATA']._serialized_start=238
  _globals['_READFILEREQUESTDATA']._serialized_end=278
  _globals['_READFILERESPONSEDATA']._serialized_start=280
  _globals['_READFILERESPONSEDATA']._serialized_end=350
  _globals['_DATANODESERVICE']._serialized_start=353
  _globals['_DATANODESERVICE']._serialized_end=487
# @@protoc_insertion_point(module_scope)

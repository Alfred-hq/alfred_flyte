# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/core/metrics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66lyteidl/core/metrics.proto\x12\rflyteidl.core\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x03\n\x04Span\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12M\n\x0bworkflow_id\x18\x03 \x01(\x0b\x32*.flyteidl.core.WorkflowExecutionIdentifierH\x00R\nworkflowId\x12\x41\n\x07node_id\x18\x04 \x01(\x0b\x32&.flyteidl.core.NodeExecutionIdentifierH\x00R\x06nodeId\x12\x41\n\x07task_id\x18\x05 \x01(\x0b\x32&.flyteidl.core.TaskExecutionIdentifierH\x00R\x06taskId\x12#\n\x0coperation_id\x18\x06 \x01(\tH\x00R\x0boperationId\x12)\n\x05spans\x18\x07 \x03(\x0b\x32\x13.flyteidl.core.SpanR\x05spansB\x04\n\x02idB\xb2\x01\n\x11\x63om.flyteidl.coreB\x0cMetricsProtoP\x01Z:github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/core\xa2\x02\x03\x46\x43X\xaa\x02\rFlyteidl.Core\xca\x02\rFlyteidl\\Core\xe2\x02\x19\x46lyteidl\\Core\\GPBMetadata\xea\x02\x0e\x46lyteidl::Coreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.core.metrics_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.flyteidl.coreB\014MetricsProtoP\001Z:github.com/flyteorg/flyte/flyteidl/gen/pb-go/flyteidl/core\242\002\003FCX\252\002\rFlyteidl.Core\312\002\rFlyteidl\\Core\342\002\031Flyteidl\\Core\\GPBMetadata\352\002\016Flyteidl::Core'
  _globals['_SPAN']._serialized_start=112
  _globals['_SPAN']._serialized_end=531
# @@protoc_insertion_point(module_scope)
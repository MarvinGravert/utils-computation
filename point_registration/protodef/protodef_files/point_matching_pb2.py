# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: point_matching.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='point_matching.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14point_matching.proto\"F\n\x05input\x12\x14\n\x0cvector_data1\x18\x01 \x03(\x02\x12\x14\n\x0cvector_data2\x18\x02 \x03(\x02\x12\x11\n\talgorithm\x18\x03 \x01(\t\"9\n\x06output\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x1f\n\nhom_matrix\x18\x02 \x03(\x0b\x32\x0b.matrix_row\"\x19\n\nmatrix_row\x12\x0b\n\x03row\x18\x01 \x03(\x02\x32\x33\n\x0cPointMatcher\x12#\n\x0epoint_matching\x12\x06.input\x1a\x07.output\"\x00\x62\x06proto3'
)




_INPUT = _descriptor.Descriptor(
  name='input',
  full_name='input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_data1', full_name='input.vector_data1', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vector_data2', full_name='input.vector_data2', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='input.algorithm', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=94,
)


_OUTPUT = _descriptor.Descriptor(
  name='output',
  full_name='output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='output.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hom_matrix', full_name='output.hom_matrix', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=153,
)


_MATRIX_ROW = _descriptor.Descriptor(
  name='matrix_row',
  full_name='matrix_row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='matrix_row.row', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=155,
  serialized_end=180,
)

_OUTPUT.fields_by_name['hom_matrix'].message_type = _MATRIX_ROW
DESCRIPTOR.message_types_by_name['input'] = _INPUT
DESCRIPTOR.message_types_by_name['output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['matrix_row'] = _MATRIX_ROW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

input = _reflection.GeneratedProtocolMessageType('input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'point_matching_pb2'
  # @@protoc_insertion_point(class_scope:input)
  })
_sym_db.RegisterMessage(input)

output = _reflection.GeneratedProtocolMessageType('output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'point_matching_pb2'
  # @@protoc_insertion_point(class_scope:output)
  })
_sym_db.RegisterMessage(output)

matrix_row = _reflection.GeneratedProtocolMessageType('matrix_row', (_message.Message,), {
  'DESCRIPTOR' : _MATRIX_ROW,
  '__module__' : 'point_matching_pb2'
  # @@protoc_insertion_point(class_scope:matrix_row)
  })
_sym_db.RegisterMessage(matrix_row)



_POINTMATCHER = _descriptor.ServiceDescriptor(
  name='PointMatcher',
  full_name='PointMatcher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=182,
  serialized_end=233,
  methods=[
  _descriptor.MethodDescriptor(
    name='point_matching',
    full_name='PointMatcher.point_matching',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POINTMATCHER)

DESCRIPTOR.services_by_name['PointMatcher'] = _POINTMATCHER

# @@protoc_insertion_point(module_scope)

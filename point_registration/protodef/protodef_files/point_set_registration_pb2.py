# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: point_set_registration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='point_set_registration.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cpoint_set_registration.proto\"`\n\x05Input\x12\x1b\n\npointSet_1\x18\x01 \x03(\x0b\x32\x07.Vector\x12\x1b\n\npointSet_2\x18\x02 \x03(\x0b\x32\x07.Vector\x12\x1d\n\talgorithm\x18\x03 \x01(\x0b\x32\n.Algorithm\"`\n\x06Output\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\"\n\x0erotationMatrix\x18\x02 \x03(\x0b\x32\n.MatrixRow\x12\"\n\x11translationVector\x18\x03 \x01(\x0b\x32\x07.Vector\"\x18\n\tMatrixRow\x12\x0b\n\x03row\x18\x01 \x03(\x02\"\x19\n\x06Vector\x12\x0f\n\x07\x65ntries\x18\x01 \x03(\x02\"\x9a\x01\n\tAlgorithm\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.Algorithm.Type\x12\x10\n\x08optimize\x18\x02 \x01(\x08\x12!\n\x06ransac\x18\x03 \x01(\x0b\x32\x11.RANSACParameters\"9\n\x04Type\x12\x08\n\x04\x41RUN\x10\x00\x12\n\n\x06KABSCH\x10\x00\x12\n\n\x06OPENCV\x10\x01\x12\x0b\n\x07UMEYAMA\x10\x01\x1a\x02\x10\x01\"9\n\x10RANSACParameters\x12\x11\n\tthreshold\x18\x01 \x01(\x02\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x32<\n\x13PointSetRegistering\x12%\n\x10registerPointSet\x12\x06.Input\x1a\x07.Output\"\x00\x62\x06proto3'
)



_ALGORITHM_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Algorithm.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ARUN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KABSCH', index=1, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPENCV', index=2, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UMEYAMA', index=3, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\020\001',
  serialized_start=379,
  serialized_end=436,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHM_TYPE)


_INPUT = _descriptor.Descriptor(
  name='Input',
  full_name='Input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pointSet_1', full_name='Input.pointSet_1', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pointSet_2', full_name='Input.pointSet_2', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='Input.algorithm', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=32,
  serialized_end=128,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Output.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotationMatrix', full_name='Output.rotationMatrix', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='translationVector', full_name='Output.translationVector', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=130,
  serialized_end=226,
)


_MATRIXROW = _descriptor.Descriptor(
  name='MatrixRow',
  full_name='MatrixRow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='MatrixRow.row', index=0,
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
  serialized_start=228,
  serialized_end=252,
)


_VECTOR = _descriptor.Descriptor(
  name='Vector',
  full_name='Vector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='Vector.entries', index=0,
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
  serialized_start=254,
  serialized_end=279,
)


_ALGORITHM = _descriptor.Descriptor(
  name='Algorithm',
  full_name='Algorithm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Algorithm.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='optimize', full_name='Algorithm.optimize', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ransac', full_name='Algorithm.ransac', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALGORITHM_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=436,
)


_RANSACPARAMETERS = _descriptor.Descriptor(
  name='RANSACParameters',
  full_name='RANSACParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='threshold', full_name='RANSACParameters.threshold', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='RANSACParameters.confidence', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=438,
  serialized_end=495,
)

_INPUT.fields_by_name['pointSet_1'].message_type = _VECTOR
_INPUT.fields_by_name['pointSet_2'].message_type = _VECTOR
_INPUT.fields_by_name['algorithm'].message_type = _ALGORITHM
_OUTPUT.fields_by_name['rotationMatrix'].message_type = _MATRIXROW
_OUTPUT.fields_by_name['translationVector'].message_type = _VECTOR
_ALGORITHM.fields_by_name['type'].enum_type = _ALGORITHM_TYPE
_ALGORITHM.fields_by_name['ransac'].message_type = _RANSACPARAMETERS
_ALGORITHM_TYPE.containing_type = _ALGORITHM
DESCRIPTOR.message_types_by_name['Input'] = _INPUT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['MatrixRow'] = _MATRIXROW
DESCRIPTOR.message_types_by_name['Vector'] = _VECTOR
DESCRIPTOR.message_types_by_name['Algorithm'] = _ALGORITHM
DESCRIPTOR.message_types_by_name['RANSACParameters'] = _RANSACPARAMETERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Input = _reflection.GeneratedProtocolMessageType('Input', (_message.Message,), {
  'DESCRIPTOR' : _INPUT,
  '__module__' : 'point_set_registration_pb2'
  # @@protoc_insertion_point(class_scope:Input)
  })
_sym_db.RegisterMessage(Input)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'point_set_registration_pb2'
  # @@protoc_insertion_point(class_scope:Output)
  })
_sym_db.RegisterMessage(Output)

MatrixRow = _reflection.GeneratedProtocolMessageType('MatrixRow', (_message.Message,), {
  'DESCRIPTOR' : _MATRIXROW,
  '__module__' : 'point_set_registration_pb2'
  # @@protoc_insertion_point(class_scope:MatrixRow)
  })
_sym_db.RegisterMessage(MatrixRow)

Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR,
  '__module__' : 'point_set_registration_pb2'
  # @@protoc_insertion_point(class_scope:Vector)
  })
_sym_db.RegisterMessage(Vector)

Algorithm = _reflection.GeneratedProtocolMessageType('Algorithm', (_message.Message,), {
  'DESCRIPTOR' : _ALGORITHM,
  '__module__' : 'point_set_registration_pb2'
  # @@protoc_insertion_point(class_scope:Algorithm)
  })
_sym_db.RegisterMessage(Algorithm)

RANSACParameters = _reflection.GeneratedProtocolMessageType('RANSACParameters', (_message.Message,), {
  'DESCRIPTOR' : _RANSACPARAMETERS,
  '__module__' : 'point_set_registration_pb2'
  # @@protoc_insertion_point(class_scope:RANSACParameters)
  })
_sym_db.RegisterMessage(RANSACParameters)


_ALGORITHM_TYPE._options = None

_POINTSETREGISTERING = _descriptor.ServiceDescriptor(
  name='PointSetRegistering',
  full_name='PointSetRegistering',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=497,
  serialized_end=557,
  methods=[
  _descriptor.MethodDescriptor(
    name='registerPointSet',
    full_name='PointSetRegistering.registerPointSet',
    index=0,
    containing_service=None,
    input_type=_INPUT,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POINTSETREGISTERING)

DESCRIPTOR.services_by_name['PointSetRegistering'] = _POINTSETREGISTERING

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/log_memory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_description_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__description__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/framework/log_memory.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n*tensorflow/core/framework/log_memory.proto\x12\ntensorflow\x1a\x32tensorflow/core/framework/tensor_description.proto\"0\n\rMemoryLogStep\x12\x0f\n\x07step_id\x18\x01 \x01(\x03\x12\x0e\n\x06handle\x18\x02 \x01(\t\"p\n\x19MemoryLogTensorAllocation\x12\x0f\n\x07step_id\x18\x01 \x01(\x03\x12\x13\n\x0bkernel_name\x18\x02 \x01(\t\x12-\n\x06tensor\x18\x03 \x01(\x0b\x32\x1d.tensorflow.TensorDescription\"L\n\x1bMemoryLogTensorDeallocation\x12\x15\n\rallocation_id\x18\x01 \x01(\x03\x12\x16\n\x0e\x61llocator_name\x18\x02 \x01(\t\"{\n\x15MemoryLogTensorOutput\x12\x0f\n\x07step_id\x18\x01 \x01(\x03\x12\x13\n\x0bkernel_name\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\x05\x12-\n\x06tensor\x18\x04 \x01(\x0b\x32\x1d.tensorflow.TensorDescription\"\x8b\x01\n\x16MemoryLogRawAllocation\x12\x0f\n\x07step_id\x18\x01 \x01(\x03\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x11\n\tnum_bytes\x18\x03 \x01(\x03\x12\x0b\n\x03ptr\x18\x04 \x01(\x04\x12\x15\n\rallocation_id\x18\x05 \x01(\x03\x12\x16\n\x0e\x61llocator_name\x18\x06 \x01(\t\"\x7f\n\x18MemoryLogRawDeallocation\x12\x0f\n\x07step_id\x18\x01 \x01(\x03\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x15\n\rallocation_id\x18\x03 \x01(\x03\x12\x16\n\x0e\x61llocator_name\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65\x66\x65rred\x18\x05 \x01(\x08\x42\x30\n\x18org.tensorflow.frameworkB\x0fLogMemoryProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__description__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MEMORYLOGSTEP = _descriptor.Descriptor(
  name='MemoryLogStep',
  full_name='tensorflow.MemoryLogStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='tensorflow.MemoryLogStep.step_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='handle', full_name='tensorflow.MemoryLogStep.handle', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=158,
)


_MEMORYLOGTENSORALLOCATION = _descriptor.Descriptor(
  name='MemoryLogTensorAllocation',
  full_name='tensorflow.MemoryLogTensorAllocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='tensorflow.MemoryLogTensorAllocation.step_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_name', full_name='tensorflow.MemoryLogTensorAllocation.kernel_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tensorflow.MemoryLogTensorAllocation.tensor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=272,
)


_MEMORYLOGTENSORDEALLOCATION = _descriptor.Descriptor(
  name='MemoryLogTensorDeallocation',
  full_name='tensorflow.MemoryLogTensorDeallocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allocation_id', full_name='tensorflow.MemoryLogTensorDeallocation.allocation_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocator_name', full_name='tensorflow.MemoryLogTensorDeallocation.allocator_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=350,
)


_MEMORYLOGTENSOROUTPUT = _descriptor.Descriptor(
  name='MemoryLogTensorOutput',
  full_name='tensorflow.MemoryLogTensorOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='tensorflow.MemoryLogTensorOutput.step_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_name', full_name='tensorflow.MemoryLogTensorOutput.kernel_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='tensorflow.MemoryLogTensorOutput.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tensorflow.MemoryLogTensorOutput.tensor', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=352,
  serialized_end=475,
)


_MEMORYLOGRAWALLOCATION = _descriptor.Descriptor(
  name='MemoryLogRawAllocation',
  full_name='tensorflow.MemoryLogRawAllocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='tensorflow.MemoryLogRawAllocation.step_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='tensorflow.MemoryLogRawAllocation.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_bytes', full_name='tensorflow.MemoryLogRawAllocation.num_bytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ptr', full_name='tensorflow.MemoryLogRawAllocation.ptr', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocation_id', full_name='tensorflow.MemoryLogRawAllocation.allocation_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocator_name', full_name='tensorflow.MemoryLogRawAllocation.allocator_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=478,
  serialized_end=617,
)


_MEMORYLOGRAWDEALLOCATION = _descriptor.Descriptor(
  name='MemoryLogRawDeallocation',
  full_name='tensorflow.MemoryLogRawDeallocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='tensorflow.MemoryLogRawDeallocation.step_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='tensorflow.MemoryLogRawDeallocation.operation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocation_id', full_name='tensorflow.MemoryLogRawDeallocation.allocation_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allocator_name', full_name='tensorflow.MemoryLogRawDeallocation.allocator_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deferred', full_name='tensorflow.MemoryLogRawDeallocation.deferred', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=619,
  serialized_end=746,
)

_MEMORYLOGTENSORALLOCATION.fields_by_name['tensor'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__description__pb2._TENSORDESCRIPTION
_MEMORYLOGTENSOROUTPUT.fields_by_name['tensor'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__description__pb2._TENSORDESCRIPTION
DESCRIPTOR.message_types_by_name['MemoryLogStep'] = _MEMORYLOGSTEP
DESCRIPTOR.message_types_by_name['MemoryLogTensorAllocation'] = _MEMORYLOGTENSORALLOCATION
DESCRIPTOR.message_types_by_name['MemoryLogTensorDeallocation'] = _MEMORYLOGTENSORDEALLOCATION
DESCRIPTOR.message_types_by_name['MemoryLogTensorOutput'] = _MEMORYLOGTENSOROUTPUT
DESCRIPTOR.message_types_by_name['MemoryLogRawAllocation'] = _MEMORYLOGRAWALLOCATION
DESCRIPTOR.message_types_by_name['MemoryLogRawDeallocation'] = _MEMORYLOGRAWDEALLOCATION

MemoryLogStep = _reflection.GeneratedProtocolMessageType('MemoryLogStep', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYLOGSTEP,
  __module__ = 'tensorflow.core.framework.log_memory_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryLogStep)
  ))
_sym_db.RegisterMessage(MemoryLogStep)

MemoryLogTensorAllocation = _reflection.GeneratedProtocolMessageType('MemoryLogTensorAllocation', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYLOGTENSORALLOCATION,
  __module__ = 'tensorflow.core.framework.log_memory_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryLogTensorAllocation)
  ))
_sym_db.RegisterMessage(MemoryLogTensorAllocation)

MemoryLogTensorDeallocation = _reflection.GeneratedProtocolMessageType('MemoryLogTensorDeallocation', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYLOGTENSORDEALLOCATION,
  __module__ = 'tensorflow.core.framework.log_memory_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryLogTensorDeallocation)
  ))
_sym_db.RegisterMessage(MemoryLogTensorDeallocation)

MemoryLogTensorOutput = _reflection.GeneratedProtocolMessageType('MemoryLogTensorOutput', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYLOGTENSOROUTPUT,
  __module__ = 'tensorflow.core.framework.log_memory_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryLogTensorOutput)
  ))
_sym_db.RegisterMessage(MemoryLogTensorOutput)

MemoryLogRawAllocation = _reflection.GeneratedProtocolMessageType('MemoryLogRawAllocation', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYLOGRAWALLOCATION,
  __module__ = 'tensorflow.core.framework.log_memory_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryLogRawAllocation)
  ))
_sym_db.RegisterMessage(MemoryLogRawAllocation)

MemoryLogRawDeallocation = _reflection.GeneratedProtocolMessageType('MemoryLogRawDeallocation', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYLOGRAWDEALLOCATION,
  __module__ = 'tensorflow.core.framework.log_memory_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryLogRawDeallocation)
  ))
_sym_db.RegisterMessage(MemoryLogRawDeallocation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\017LogMemoryProtosP\001\370\001\001'))
# @@protoc_insertion_point(module_scope)

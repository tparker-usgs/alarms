# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alarm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alarm.proto',
  package='gov.usgs.volcanoes.alarm',
  serialized_pb='\n\x0b\x61larm.proto\x12\x18gov.usgs.volcanoes.alarm\"\xc7\x01\n\x05\x41larm\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\nattachment\x18\x02 \x01(\x0c\x12\x34\n\x05state\x18\x03 \x01(\x0e\x32%.gov.usgs.volcanoes.alarm.Alarm.State\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\"7\n\x05State\x12\x06\n\x02OK\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\x0c\n\x08\x43RITICAL\x10\x02\x12\x0b\n\x07UNKNOWN\x10\x03')



_ALARM_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='gov.usgs.volcanoes.alarm.Alarm.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=186,
  serialized_end=241,
)


_ALARM = _descriptor.Descriptor(
  name='Alarm',
  full_name='gov.usgs.volcanoes.alarm.Alarm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='gov.usgs.volcanoes.alarm.Alarm.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attachment', full_name='gov.usgs.volcanoes.alarm.Alarm.attachment', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='gov.usgs.volcanoes.alarm.Alarm.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='region', full_name='gov.usgs.volcanoes.alarm.Alarm.region', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='gov.usgs.volcanoes.alarm.Alarm.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='gov.usgs.volcanoes.alarm.Alarm.type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ALARM_STATE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=42,
  serialized_end=241,
)

_ALARM.fields_by_name['state'].enum_type = _ALARM_STATE
_ALARM_STATE.containing_type = _ALARM;
DESCRIPTOR.message_types_by_name['Alarm'] = _ALARM

class Alarm(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ALARM

  # @@protoc_insertion_point(class_scope:gov.usgs.volcanoes.alarm.Alarm)


# @@protoc_insertion_point(module_scope)

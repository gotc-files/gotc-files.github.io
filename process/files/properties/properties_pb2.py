# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files/properties/properties.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from files.common import common_pb2 as files_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!files/properties/properties.proto\x1a\x19\x66iles/common/common.proto\"\xb7\x02\n\nProperties\x12(\n\nproperties\x18\x01 \x03(\x0b\x32\x14.Properties.Property\x1aU\n\x08Property\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12&\n\x04info\x18\x02 \x01(\x0b\x32\x18.Properties.PropertyInfo\x1a\x80\x01\n\x0cPropertyInfo\x12\x18\n\x10name_placeholder\x18\x01 \x01(\t\x12\x1f\n\x17\x64\x65scription_placeholder\x18\x02 \x01(\t\x12&\n\x04type\x18\x03 \x01(\x0e\x32\x18.Properties.PropertyType\x12\r\n\x05image\x18\x04 \x01(\t\"%\n\x0cPropertyType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04GEAR\x10\x04\x62\x06proto3')



_PROPERTIES = DESCRIPTOR.message_types_by_name['Properties']
_PROPERTIES_PROPERTY = _PROPERTIES.nested_types_by_name['Property']
_PROPERTIES_PROPERTYINFO = _PROPERTIES.nested_types_by_name['PropertyInfo']
_PROPERTIES_PROPERTYTYPE = _PROPERTIES.enum_types_by_name['PropertyType']
Properties = _reflection.GeneratedProtocolMessageType('Properties', (_message.Message,), {

  'Property' : _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), {
    'DESCRIPTOR' : _PROPERTIES_PROPERTY,
    '__module__' : 'files.properties.properties_pb2'
    # @@protoc_insertion_point(class_scope:Properties.Property)
    })
  ,

  'PropertyInfo' : _reflection.GeneratedProtocolMessageType('PropertyInfo', (_message.Message,), {
    'DESCRIPTOR' : _PROPERTIES_PROPERTYINFO,
    '__module__' : 'files.properties.properties_pb2'
    # @@protoc_insertion_point(class_scope:Properties.PropertyInfo)
    })
  ,
  'DESCRIPTOR' : _PROPERTIES,
  '__module__' : 'files.properties.properties_pb2'
  # @@protoc_insertion_point(class_scope:Properties)
  })
_sym_db.RegisterMessage(Properties)
_sym_db.RegisterMessage(Properties.Property)
_sym_db.RegisterMessage(Properties.PropertyInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROPERTIES._serialized_start=65
  _PROPERTIES._serialized_end=376
  _PROPERTIES_PROPERTY._serialized_start=121
  _PROPERTIES_PROPERTY._serialized_end=206
  _PROPERTIES_PROPERTYINFO._serialized_start=209
  _PROPERTIES_PROPERTYINFO._serialized_end=337
  _PROPERTIES_PROPERTYTYPE._serialized_start=339
  _PROPERTIES_PROPERTYTYPE._serialized_end=376
# @@protoc_insertion_point(module_scope)

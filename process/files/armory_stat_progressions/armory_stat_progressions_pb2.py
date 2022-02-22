# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files/armory_stat_progressions/armory_stat_progressions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from files.common import common_pb2 as files_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=files/armory_stat_progressions/armory_stat_progressions.proto\x1a\x19\x66iles/common/common.proto\"\xc8\x03\n\x16\x41rmoryStatProgressions\x12O\n\x18\x61rmory_stat_progressions\x18\x01 \x03(\x0b\x32-.ArmoryStatProgressions.ArmoryStatProgression\x1aZ\n\x15\x41rmoryStatProgression\x12\n\n\x02id\x18\x01 \x01(\x06\x12\x35\n\x04info\x18\x02 \x01(\x0b\x32\'.ArmoryStatProgressions.ProgressionInfo\x1a\x81\x01\n\x0fProgressionInfo\x12\x33\n\tint_stats\x18\x01 \x01(\x0b\x32 .ArmoryStatProgressions.IntStats\x12\x39\n\x0c\x64ouble_stats\x18\x02 \x01(\x0b\x32#.ArmoryStatProgressions.DoubleStats\x1a<\n\x08IntStats\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12\r\n\x05stats\x18\x02 \x03(\x03\x1a?\n\x0b\x44oubleStats\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12\r\n\x05stats\x18\x02 \x03(\x01\x62\x06proto3')



_ARMORYSTATPROGRESSIONS = DESCRIPTOR.message_types_by_name['ArmoryStatProgressions']
_ARMORYSTATPROGRESSIONS_ARMORYSTATPROGRESSION = _ARMORYSTATPROGRESSIONS.nested_types_by_name['ArmoryStatProgression']
_ARMORYSTATPROGRESSIONS_PROGRESSIONINFO = _ARMORYSTATPROGRESSIONS.nested_types_by_name['ProgressionInfo']
_ARMORYSTATPROGRESSIONS_INTSTATS = _ARMORYSTATPROGRESSIONS.nested_types_by_name['IntStats']
_ARMORYSTATPROGRESSIONS_DOUBLESTATS = _ARMORYSTATPROGRESSIONS.nested_types_by_name['DoubleStats']
ArmoryStatProgressions = _reflection.GeneratedProtocolMessageType('ArmoryStatProgressions', (_message.Message,), {

  'ArmoryStatProgression' : _reflection.GeneratedProtocolMessageType('ArmoryStatProgression', (_message.Message,), {
    'DESCRIPTOR' : _ARMORYSTATPROGRESSIONS_ARMORYSTATPROGRESSION,
    '__module__' : 'files.armory_stat_progressions.armory_stat_progressions_pb2'
    # @@protoc_insertion_point(class_scope:ArmoryStatProgressions.ArmoryStatProgression)
    })
  ,

  'ProgressionInfo' : _reflection.GeneratedProtocolMessageType('ProgressionInfo', (_message.Message,), {
    'DESCRIPTOR' : _ARMORYSTATPROGRESSIONS_PROGRESSIONINFO,
    '__module__' : 'files.armory_stat_progressions.armory_stat_progressions_pb2'
    # @@protoc_insertion_point(class_scope:ArmoryStatProgressions.ProgressionInfo)
    })
  ,

  'IntStats' : _reflection.GeneratedProtocolMessageType('IntStats', (_message.Message,), {
    'DESCRIPTOR' : _ARMORYSTATPROGRESSIONS_INTSTATS,
    '__module__' : 'files.armory_stat_progressions.armory_stat_progressions_pb2'
    # @@protoc_insertion_point(class_scope:ArmoryStatProgressions.IntStats)
    })
  ,

  'DoubleStats' : _reflection.GeneratedProtocolMessageType('DoubleStats', (_message.Message,), {
    'DESCRIPTOR' : _ARMORYSTATPROGRESSIONS_DOUBLESTATS,
    '__module__' : 'files.armory_stat_progressions.armory_stat_progressions_pb2'
    # @@protoc_insertion_point(class_scope:ArmoryStatProgressions.DoubleStats)
    })
  ,
  'DESCRIPTOR' : _ARMORYSTATPROGRESSIONS,
  '__module__' : 'files.armory_stat_progressions.armory_stat_progressions_pb2'
  # @@protoc_insertion_point(class_scope:ArmoryStatProgressions)
  })
_sym_db.RegisterMessage(ArmoryStatProgressions)
_sym_db.RegisterMessage(ArmoryStatProgressions.ArmoryStatProgression)
_sym_db.RegisterMessage(ArmoryStatProgressions.ProgressionInfo)
_sym_db.RegisterMessage(ArmoryStatProgressions.IntStats)
_sym_db.RegisterMessage(ArmoryStatProgressions.DoubleStats)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ARMORYSTATPROGRESSIONS._serialized_start=93
  _ARMORYSTATPROGRESSIONS._serialized_end=549
  _ARMORYSTATPROGRESSIONS_ARMORYSTATPROGRESSION._serialized_start=200
  _ARMORYSTATPROGRESSIONS_ARMORYSTATPROGRESSION._serialized_end=290
  _ARMORYSTATPROGRESSIONS_PROGRESSIONINFO._serialized_start=293
  _ARMORYSTATPROGRESSIONS_PROGRESSIONINFO._serialized_end=422
  _ARMORYSTATPROGRESSIONS_INTSTATS._serialized_start=424
  _ARMORYSTATPROGRESSIONS_INTSTATS._serialized_end=484
  _ARMORYSTATPROGRESSIONS_DOUBLESTATS._serialized_start=486
  _ARMORYSTATPROGRESSIONS_DOUBLESTATS._serialized_end=549
# @@protoc_insertion_point(module_scope)

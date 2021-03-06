# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files/hero_traits/hero_traits.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from files.common import common_pb2 as files_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#files/hero_traits/hero_traits.proto\x1a\x19\x66iles/common/common.proto\"\x9c\x02\n\nHeroTraits\x12*\n\x0bhero_traits\x18\x01 \x03(\x0b\x32\x15.HeroTraits.HeroTrait\x1aW\n\tHeroTrait\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12\'\n\x04info\x18\x02 \x01(\x0b\x32\x19.HeroTraits.HeroTraitInfo\x1a\x88\x01\n\rHeroTraitInfo\x12\x18\n\x10name_placeholder\x18\x01 \x01(\t\x12\x1f\n\x17\x64\x65scription_placeholder\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12-\n\x14\x65vent_bonus_modifier\x18\x04 \x01(\x0b\x32\x0f.ObjectIdentityb\x06proto3')



_HEROTRAITS = DESCRIPTOR.message_types_by_name['HeroTraits']
_HEROTRAITS_HEROTRAIT = _HEROTRAITS.nested_types_by_name['HeroTrait']
_HEROTRAITS_HEROTRAITINFO = _HEROTRAITS.nested_types_by_name['HeroTraitInfo']
HeroTraits = _reflection.GeneratedProtocolMessageType('HeroTraits', (_message.Message,), {

  'HeroTrait' : _reflection.GeneratedProtocolMessageType('HeroTrait', (_message.Message,), {
    'DESCRIPTOR' : _HEROTRAITS_HEROTRAIT,
    '__module__' : 'files.hero_traits.hero_traits_pb2'
    # @@protoc_insertion_point(class_scope:HeroTraits.HeroTrait)
    })
  ,

  'HeroTraitInfo' : _reflection.GeneratedProtocolMessageType('HeroTraitInfo', (_message.Message,), {
    'DESCRIPTOR' : _HEROTRAITS_HEROTRAITINFO,
    '__module__' : 'files.hero_traits.hero_traits_pb2'
    # @@protoc_insertion_point(class_scope:HeroTraits.HeroTraitInfo)
    })
  ,
  'DESCRIPTOR' : _HEROTRAITS,
  '__module__' : 'files.hero_traits.hero_traits_pb2'
  # @@protoc_insertion_point(class_scope:HeroTraits)
  })
_sym_db.RegisterMessage(HeroTraits)
_sym_db.RegisterMessage(HeroTraits.HeroTrait)
_sym_db.RegisterMessage(HeroTraits.HeroTraitInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEROTRAITS._serialized_start=67
  _HEROTRAITS._serialized_end=351
  _HEROTRAITS_HEROTRAIT._serialized_start=125
  _HEROTRAITS_HEROTRAIT._serialized_end=212
  _HEROTRAITS_HEROTRAITINFO._serialized_start=215
  _HEROTRAITS_HEROTRAITINFO._serialized_end=351
# @@protoc_insertion_point(module_scope)

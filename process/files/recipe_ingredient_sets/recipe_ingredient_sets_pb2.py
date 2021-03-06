# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files/recipe_ingredient_sets/recipe_ingredient_sets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from files.common import common_pb2 as files_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9files/recipe_ingredient_sets/recipe_ingredient_sets.proto\x1a\x19\x66iles/common/common.proto\"\xa2\x04\n\x14RecipeIngredientSets\x12I\n\x16recipe_ingredient_sets\x18\x01 \x03(\x0b\x32).RecipeIngredientSets.RecipeIngredientSet\x1au\n\x13RecipeIngredientSet\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12;\n\x04info\x18\x02 \x01(\x0b\x32-.RecipeIngredientSets.RecipeIngredientSetInfo\x1a\x8d\x01\n\x17RecipeIngredientSetInfo\x12<\n\x0bingredients\x18\x01 \x01(\x0b\x32\'.RecipeIngredientSets.RecipeIngredients\x12\x34\n\x07rewards\x18\x02 \x01(\x0b\x32#.RecipeIngredientSets.RecipeRewards\x1aP\n\x11RecipeIngredients\x12;\n\x0bingredients\x18\x01 \x03(\x0b\x32&.RecipeIngredientSets.RecipeIngredient\x1aU\n\x10RecipeIngredient\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x05\x1a\x0f\n\rRecipeRewardsb\x06proto3')



_RECIPEINGREDIENTSETS = DESCRIPTOR.message_types_by_name['RecipeIngredientSets']
_RECIPEINGREDIENTSETS_RECIPEINGREDIENTSET = _RECIPEINGREDIENTSETS.nested_types_by_name['RecipeIngredientSet']
_RECIPEINGREDIENTSETS_RECIPEINGREDIENTSETINFO = _RECIPEINGREDIENTSETS.nested_types_by_name['RecipeIngredientSetInfo']
_RECIPEINGREDIENTSETS_RECIPEINGREDIENTS = _RECIPEINGREDIENTSETS.nested_types_by_name['RecipeIngredients']
_RECIPEINGREDIENTSETS_RECIPEINGREDIENT = _RECIPEINGREDIENTSETS.nested_types_by_name['RecipeIngredient']
_RECIPEINGREDIENTSETS_RECIPEREWARDS = _RECIPEINGREDIENTSETS.nested_types_by_name['RecipeRewards']
RecipeIngredientSets = _reflection.GeneratedProtocolMessageType('RecipeIngredientSets', (_message.Message,), {

  'RecipeIngredientSet' : _reflection.GeneratedProtocolMessageType('RecipeIngredientSet', (_message.Message,), {
    'DESCRIPTOR' : _RECIPEINGREDIENTSETS_RECIPEINGREDIENTSET,
    '__module__' : 'files.recipe_ingredient_sets.recipe_ingredient_sets_pb2'
    # @@protoc_insertion_point(class_scope:RecipeIngredientSets.RecipeIngredientSet)
    })
  ,

  'RecipeIngredientSetInfo' : _reflection.GeneratedProtocolMessageType('RecipeIngredientSetInfo', (_message.Message,), {
    'DESCRIPTOR' : _RECIPEINGREDIENTSETS_RECIPEINGREDIENTSETINFO,
    '__module__' : 'files.recipe_ingredient_sets.recipe_ingredient_sets_pb2'
    # @@protoc_insertion_point(class_scope:RecipeIngredientSets.RecipeIngredientSetInfo)
    })
  ,

  'RecipeIngredients' : _reflection.GeneratedProtocolMessageType('RecipeIngredients', (_message.Message,), {
    'DESCRIPTOR' : _RECIPEINGREDIENTSETS_RECIPEINGREDIENTS,
    '__module__' : 'files.recipe_ingredient_sets.recipe_ingredient_sets_pb2'
    # @@protoc_insertion_point(class_scope:RecipeIngredientSets.RecipeIngredients)
    })
  ,

  'RecipeIngredient' : _reflection.GeneratedProtocolMessageType('RecipeIngredient', (_message.Message,), {
    'DESCRIPTOR' : _RECIPEINGREDIENTSETS_RECIPEINGREDIENT,
    '__module__' : 'files.recipe_ingredient_sets.recipe_ingredient_sets_pb2'
    # @@protoc_insertion_point(class_scope:RecipeIngredientSets.RecipeIngredient)
    })
  ,

  'RecipeRewards' : _reflection.GeneratedProtocolMessageType('RecipeRewards', (_message.Message,), {
    'DESCRIPTOR' : _RECIPEINGREDIENTSETS_RECIPEREWARDS,
    '__module__' : 'files.recipe_ingredient_sets.recipe_ingredient_sets_pb2'
    # @@protoc_insertion_point(class_scope:RecipeIngredientSets.RecipeRewards)
    })
  ,
  'DESCRIPTOR' : _RECIPEINGREDIENTSETS,
  '__module__' : 'files.recipe_ingredient_sets.recipe_ingredient_sets_pb2'
  # @@protoc_insertion_point(class_scope:RecipeIngredientSets)
  })
_sym_db.RegisterMessage(RecipeIngredientSets)
_sym_db.RegisterMessage(RecipeIngredientSets.RecipeIngredientSet)
_sym_db.RegisterMessage(RecipeIngredientSets.RecipeIngredientSetInfo)
_sym_db.RegisterMessage(RecipeIngredientSets.RecipeIngredients)
_sym_db.RegisterMessage(RecipeIngredientSets.RecipeIngredient)
_sym_db.RegisterMessage(RecipeIngredientSets.RecipeRewards)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECIPEINGREDIENTSETS._serialized_start=89
  _RECIPEINGREDIENTSETS._serialized_end=635
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENTSET._serialized_start=188
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENTSET._serialized_end=305
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENTSETINFO._serialized_start=308
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENTSETINFO._serialized_end=449
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENTS._serialized_start=451
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENTS._serialized_end=531
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENT._serialized_start=533
  _RECIPEINGREDIENTSETS_RECIPEINGREDIENT._serialized_end=618
  _RECIPEINGREDIENTSETS_RECIPEREWARDS._serialized_start=620
  _RECIPEINGREDIENTSETS_RECIPEREWARDS._serialized_end=635
# @@protoc_insertion_point(module_scope)

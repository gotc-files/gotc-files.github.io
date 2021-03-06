# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: files/recipes/recipies.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from files.common import common_pb2 as files_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66iles/recipes/recipies.proto\x1a\x19\x66iles/common/common.proto\"\xff\x03\n\x07Recipes\x12 \n\x07recipes\x18\x01 \x03(\x0b\x32\x0f.Recipes.Recipe\x1aN\n\x06Recipe\x12!\n\x08identity\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12!\n\x04info\x18\x02 \x01(\x0b\x32\x13.Recipes.RecipeInfo\x1a\x81\x03\n\nRecipeInfo\x12$\n\x0bingredients\x18\x01 \x01(\x0b\x32\x0f.ObjectIdentity\x12\r\n\x05image\x18\x02 \x01(\t\x12\x15\n\roverlay_image\x18\x03 \x01(\t\x12\x16\n\x0etarget_quality\x18\x04 \x01(\x05\x12\x15\n\runknown_1_int\x18\x05 \x01(\x05\x12\r\n\x05limit\x18\x06 \x01(\x05\x12\x18\n\x10name_placeholder\x18\x07 \x01(\t\x12\x1f\n\x17\x64\x65scription_placeholder\x18\x08 \x01(\t\x12\x15\n\runknown_2_int\x18\t \x01(\x05\x12\x14\n\x0c\x65vent_points\x18\n \x01(\x05\x12\x12\n\nevent_name\x18\x0b \x01(\t\x12&\n\rdisplay_group\x18\x0c \x01(\x0b\x32\x0f.ObjectIdentity\x12\x17\n\x0ftarget_quantity\x18\r \x01(\x05\x12\x15\n\rsort_priority\x18\x0e \x01(\x05\x12\x15\n\runknown_3_int\x18\x0f \x01(\x05\x62\x06proto3')



_RECIPES = DESCRIPTOR.message_types_by_name['Recipes']
_RECIPES_RECIPE = _RECIPES.nested_types_by_name['Recipe']
_RECIPES_RECIPEINFO = _RECIPES.nested_types_by_name['RecipeInfo']
Recipes = _reflection.GeneratedProtocolMessageType('Recipes', (_message.Message,), {

  'Recipe' : _reflection.GeneratedProtocolMessageType('Recipe', (_message.Message,), {
    'DESCRIPTOR' : _RECIPES_RECIPE,
    '__module__' : 'files.recipes.recipies_pb2'
    # @@protoc_insertion_point(class_scope:Recipes.Recipe)
    })
  ,

  'RecipeInfo' : _reflection.GeneratedProtocolMessageType('RecipeInfo', (_message.Message,), {
    'DESCRIPTOR' : _RECIPES_RECIPEINFO,
    '__module__' : 'files.recipes.recipies_pb2'
    # @@protoc_insertion_point(class_scope:Recipes.RecipeInfo)
    })
  ,
  'DESCRIPTOR' : _RECIPES,
  '__module__' : 'files.recipes.recipies_pb2'
  # @@protoc_insertion_point(class_scope:Recipes)
  })
_sym_db.RegisterMessage(Recipes)
_sym_db.RegisterMessage(Recipes.Recipe)
_sym_db.RegisterMessage(Recipes.RecipeInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECIPES._serialized_start=60
  _RECIPES._serialized_end=571
  _RECIPES_RECIPE._serialized_start=105
  _RECIPES_RECIPE._serialized_end=183
  _RECIPES_RECIPEINFO._serialized_start=186
  _RECIPES_RECIPEINFO._serialized_end=571
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_components_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66ile_components_service.proto\"v\n\rFileComponent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\x12\x12\n\nstart_line\x18\x04 \x01(\x05\x12\x10\n\x08\x65nd_line\x18\x05 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\"9\n\x0e\x46ileComponents\x12\'\n\x0f\x66ile_components\x18\x01 \x03(\x0b\x32\x0e.FileComponent\".\n\x10\x46ileComponentIds\x12\x1a\n\x12\x66ile_component_ids\x18\x01 \x03(\x05\"4\n\rUserFilePaths\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nfile_paths\x18\x02 \x03(\t2\x89\x01\n\x15\x46ileComponentsService\x12\x37\n\x14\x43reateFileComponents\x12\x0e.UserFilePaths\x1a\x0f.FileComponents\x12\x37\n\x11GetFileComponents\x12\x11.FileComponentIds\x1a\x0f.FileComponentsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_components_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILECOMPONENT']._serialized_start=33
  _globals['_FILECOMPONENT']._serialized_end=151
  _globals['_FILECOMPONENTS']._serialized_start=153
  _globals['_FILECOMPONENTS']._serialized_end=210
  _globals['_FILECOMPONENTIDS']._serialized_start=212
  _globals['_FILECOMPONENTIDS']._serialized_end=258
  _globals['_USERFILEPATHS']._serialized_start=260
  _globals['_USERFILEPATHS']._serialized_end=312
  _globals['_FILECOMPONENTSSERVICE']._serialized_start=315
  _globals['_FILECOMPONENTSSERVICE']._serialized_end=452
# @@protoc_insertion_point(module_scope)

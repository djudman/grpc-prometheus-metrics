# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello_world.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x11hello_world.proto\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"4\n\x17MultipleHelloResRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03res\x18\x02 \x01(\x05\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xef\x01\n\x07Greeter\x12(\n\x08SayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x12@\n\x13SayHelloUnaryStream\x12\x18.MultipleHelloResRequest\x1a\x0b.HelloReply\"\x00\x30\x01\x12\x35\n\x13SayHelloStreamUnary\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00(\x01\x12\x41\n\x12SayHelloBidiStream\x12\x18.MultipleHelloResRequest\x1a\x0b.HelloReply\"\x00(\x01\x30\x01\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_world_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _HELLOREQUEST._serialized_start = 21
    _HELLOREQUEST._serialized_end = 49
    _MULTIPLEHELLORESREQUEST._serialized_start = 51
    _MULTIPLEHELLORESREQUEST._serialized_end = 103
    _HELLOREPLY._serialized_start = 105
    _HELLOREPLY._serialized_end = 134
    _GREETER._serialized_start = 137
    _GREETER._serialized_end = 376
# @@protoc_insertion_point(module_scope)

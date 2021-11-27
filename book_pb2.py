# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='book',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbook.proto\x12\x04\x62ook\x1a\x1bgoogle/protobuf/empty.proto\".\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04user\x18\x03 \x01(\x03\"\x11\n\x0f\x42ookListRequest\"0\n\x13\x42ookRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05token\x18\x02 \x01(\t2\xed\x01\n\x0e\x42ookController\x12-\n\x04List\x12\x15.book.BookListRequest\x1a\n.book.Book\"\x00\x30\x01\x12\"\n\x06\x43reate\x12\n.book.Book\x1a\n.book.Book\"\x00\x12\x33\n\x08Retrieve\x12\x19.book.BookRetrieveRequest\x1a\n.book.Book\"\x00\x12\"\n\x06Update\x12\n.book.Book\x1a\n.book.Book\"\x00\x12/\n\x07\x44\x65stroy\x12\n.book.Book\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='book.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.Book.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='book.Book.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='book.Book.user', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=49,
  serialized_end=95,
)


_BOOKLISTREQUEST = _descriptor.Descriptor(
  name='BookListRequest',
  full_name='book.BookListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=97,
  serialized_end=114,
)


_BOOKRETRIEVEREQUEST = _descriptor.Descriptor(
  name='BookRetrieveRequest',
  full_name='book.BookRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='book.BookRetrieveRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='book.BookRetrieveRequest.token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=116,
  serialized_end=164,
)

DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['BookListRequest'] = _BOOKLISTREQUEST
DESCRIPTOR.message_types_by_name['BookRetrieveRequest'] = _BOOKRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.Book)
  })
_sym_db.RegisterMessage(Book)

BookListRequest = _reflection.GeneratedProtocolMessageType('BookListRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKLISTREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookListRequest)
  })
_sym_db.RegisterMessage(BookListRequest)

BookRetrieveRequest = _reflection.GeneratedProtocolMessageType('BookRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRETRIEVEREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:book.BookRetrieveRequest)
  })
_sym_db.RegisterMessage(BookRetrieveRequest)



_BOOKCONTROLLER = _descriptor.ServiceDescriptor(
  name='BookController',
  full_name='book.BookController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=167,
  serialized_end=404,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='book.BookController.List',
    index=0,
    containing_service=None,
    input_type=_BOOKLISTREQUEST,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='book.BookController.Create',
    index=1,
    containing_service=None,
    input_type=_BOOK,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='book.BookController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_BOOKRETRIEVEREQUEST,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='book.BookController.Update',
    index=3,
    containing_service=None,
    input_type=_BOOK,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='book.BookController.Destroy',
    index=4,
    containing_service=None,
    input_type=_BOOK,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKCONTROLLER)

DESCRIPTOR.services_by_name['BookController'] = _BOOKCONTROLLER

# @@protoc_insertion_point(module_scope)

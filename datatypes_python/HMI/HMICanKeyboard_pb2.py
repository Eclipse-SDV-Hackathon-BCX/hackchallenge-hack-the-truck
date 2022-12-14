# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HMI/HMICanKeyboard.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import header_pb2 as header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='HMI/HMICanKeyboard.proto',
  package='pb.HMI',
  syntax='proto2',
  serialized_pb=_b('\n\x18HMI/HMICanKeyboard.proto\x12\x06pb.HMI\x1a\x0cheader.proto\"\xf8\t\n\x13HmiCanKeyboardState\x12\x1a\n\x06header\x18\x01 \x01(\x0b\x32\n.pb.Header\x12]\n\x15\x43\x61nKeyboard_Button_01\x18\x02 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_02\x18\x03 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_03\x18\x04 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_04\x18\x05 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_05\x18\x06 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_06\x18\x07 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_07\x18\x08 \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_08\x18\t \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_09\x18\n \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_10\x18\x0b \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_11\x18\x0c \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\x12]\n\x15\x43\x61nKeyboard_Button_12\x18\r \x01(\x0e\x32\x30.pb.HMI.HmiCanKeyboardState.can_keyboard_state_t:\x0c\x42UTTON_UNDEF\"Q\n\x14\x63\x61n_keyboard_state_t\x12\x10\n\x0c\x42UTTON_UNDEF\x10\x00\x12\x13\n\x0f\x42UTTON_RELEASED\x10\x01\x12\x12\n\x0e\x42UTTON_CLICKED\x10\x02')
  ,
  dependencies=[header__pb2.DESCRIPTOR,])



_HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T = _descriptor.EnumDescriptor(
  name='can_keyboard_state_t',
  full_name='pb.HMI.HmiCanKeyboardState.can_keyboard_state_t',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUTTON_UNDEF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_RELEASED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_CLICKED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1242,
  serialized_end=1323,
)
_sym_db.RegisterEnumDescriptor(_HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T)


_HMICANKEYBOARDSTATE = _descriptor.Descriptor(
  name='HmiCanKeyboardState',
  full_name='pb.HMI.HmiCanKeyboardState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='pb.HMI.HmiCanKeyboardState.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_01', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_01', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_02', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_02', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_03', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_03', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_04', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_04', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_05', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_05', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_06', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_06', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_07', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_07', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_08', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_08', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_09', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_09', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_10', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_10', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_11', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_11', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CanKeyboard_Button_12', full_name='pb.HMI.HmiCanKeyboardState.CanKeyboard_Button_12', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=1323,
)

_HMICANKEYBOARDSTATE.fields_by_name['header'].message_type = header__pb2._HEADER
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_01'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_02'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_03'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_04'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_05'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_06'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_07'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_08'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_09'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_10'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_11'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE.fields_by_name['CanKeyboard_Button_12'].enum_type = _HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T
_HMICANKEYBOARDSTATE_CAN_KEYBOARD_STATE_T.containing_type = _HMICANKEYBOARDSTATE
DESCRIPTOR.message_types_by_name['HmiCanKeyboardState'] = _HMICANKEYBOARDSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HmiCanKeyboardState = _reflection.GeneratedProtocolMessageType('HmiCanKeyboardState', (_message.Message,), dict(
  DESCRIPTOR = _HMICANKEYBOARDSTATE,
  __module__ = 'HMI.HMICanKeyboard_pb2'
  # @@protoc_insertion_point(class_scope:pb.HMI.HmiCanKeyboardState)
  ))
_sym_db.RegisterMessage(HmiCanKeyboardState)


# @@protoc_insertion_point(module_scope)

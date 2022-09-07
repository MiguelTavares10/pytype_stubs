import types
import typing

import genpy
import geometry_msgs.msg
import std_msgs.msg

class WrenchStamped(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    header: std_msgs.msg.Header
    wrench: geometry_msgs.msg.Wrench

    def __init__(
        self,
        header: std_msgs.msg.Header = ...,
        wrench: geometry_msgs.msg.Wrench = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> WrenchStamped: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> WrenchStamped: ...
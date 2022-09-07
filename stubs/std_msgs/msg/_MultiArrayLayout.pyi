import types
import typing

import genpy
import std_msgs.msg

class MultiArrayLayout(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    dim: typing.List[std_msgs.msg.MultiArrayDimension]
    data_offset: int

    def __init__(
        self,
        dim: typing.List[std_msgs.msg.MultiArrayDimension] = ...,
        data_offset: int = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> MultiArrayLayout: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> MultiArrayLayout: ...

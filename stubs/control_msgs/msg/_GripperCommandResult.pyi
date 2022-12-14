import types
import typing

import genpy

class GripperCommandResult(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    position: float
    effort: float
    stalled: bool
    reached_goal: bool

    def __init__(
        self,
        position: float = ...,
        effort: float = ...,
        stalled: bool = ...,
        reached_goal: bool = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> GripperCommandResult: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> GripperCommandResult: ...

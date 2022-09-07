import types
import typing

import genpy
import geometry_msgs.msg
import shape_msgs.msg

class Mesh(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    triangles: typing.List[shape_msgs.msg.MeshTriangle]
    vertices: typing.List[geometry_msgs.msg.Point]

    def __init__(
        self,
        triangles: typing.List[shape_msgs.msg.MeshTriangle] = ...,
        vertices: typing.List[geometry_msgs.msg.Point] = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> Mesh: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> Mesh: ...

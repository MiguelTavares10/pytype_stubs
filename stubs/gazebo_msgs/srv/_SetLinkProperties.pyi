import types
import typing

import genpy
import geometry_msgs.msg

class SetLinkPropertiesRequest(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    link_name: str
    com: geometry_msgs.msg.Pose
    gravity_mode: bool
    mass: float
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float

    def __init__(
        self,
        link_name: str = ...,
        com: geometry_msgs.msg.Pose = ...,
        gravity_mode: bool = ...,
        mass: float = ...,
        ixx: float = ...,
        ixy: float = ...,
        ixz: float = ...,
        iyy: float = ...,
        iyz: float = ...,
        izz: float = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetLinkPropertiesRequest: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetLinkPropertiesRequest: ...

class SetLinkPropertiesResponse(genpy.Message):
    _md5sum: str
    _type: str
    _has_header: bool
    _full_text: str
    __slots__: typing.List[str]
    _slot_types: typing.List[str]

    # Fields
    success: bool
    status_message: str

    def __init__(
        self,
        success: bool = ...,
        status_message: str = ...,
        *args: typing.Any,
        **kwds: typing.Any,
    ) -> None: ...
    def _get_types(self) -> typing.List[str]: ...
    def serialize(self, buff: typing.BinaryIO) -> None: ...
    def deserialize(self, str: bytes) -> SetLinkPropertiesResponse: ...
    def serialize_numpy(self, buff: typing.BinaryIO, numpy: types.ModuleType) -> None: ...
    def deserialize_numpy(self, str: bytes, numpy: types.ModuleType) -> SetLinkPropertiesResponse: ...

class SetLinkProperties(object):
    _type: str
    _md5sum: str
    _request_class = SetLinkPropertiesRequest
    _response_class = SetLinkPropertiesResponse

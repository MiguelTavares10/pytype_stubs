from typing import Callable, Dict, Iterator, List, Optional, Sequence, Tuple

from genmsg.msg_loader import MsgContext, MsgSpec

INDENT: str

def get_registered_ex(msg_context: MsgContext, type_: str) -> MsgSpec: ...

class Special:
    constructor: str = ...
    post_deserialize: str = ...
    import_str: str = ...
    def __init__(
        self, constructor: str, post_deserialize: str, import_str: str
    ) -> None: ...
    def get_post_deserialize(self, varname: str) -> Optional[str]: ...

def is_special(type_: str) -> bool: ...
def get_special(type_: str) -> Optional[Special]: ...
def default_value(
    msg_context: MsgContext, field_type: str, default_package: str
) -> str: ...
def flatten(msg_context: MsgContext, msg: MsgSpec) -> MsgSpec: ...
def make_python_safe(spec: MsgSpec) -> MsgSpec: ...
def compute_post_deserialize(type_: str, varname: str) -> Optional[str]: ...
def compute_constructor(
    msg_context: MsgContext, package: str, type_: str
) -> Optional[str]: ...
def compute_pkg_type(package: str, type_: str) -> Tuple[str, str]: ...
def compute_import(msg_context: MsgContext, package: str, type_: str) -> List[str]: ...
def compute_full_text_escaped(msg_context: MsgContext, spec: MsgSpec) -> str: ...
def next_var() -> str: ...
def reset_var() -> None: ...
def push_context(context: MsgContext) -> None: ...
def pop_context() -> None: ...
def len_serializer_generator(
    var: str, is_string: bool, serialize: bool
) -> Iterator[str]: ...
def string_serializer_generator(
    package: str, type_: str, name: str, serialize: bool
) -> Iterator[str]: ...
def array_serializer_generator(
    msg_context: MsgContext,
    package: str,
    type_: str,
    name: str,
    serialize: bool,
    is_numpy: bool,
) -> Iterator[str]: ...
def complex_serializer_generator(
    msg_context: MsgContext,
    package: str,
    type_: str,
    name: str,
    serialize: bool,
    is_numpy: bool,
) -> Iterator[str]: ...
def simple_serializer_generator(
    msg_context: MsgContext, spec: MsgSpec, start: int, end: int, serialize: bool
) -> Iterator[str]: ...
def serializer_generator(
    msg_context: MsgContext, spec: MsgSpec, serialize: bool, is_numpy: bool
) -> Iterator[str]: ...
def serialize_fn_generator(
    msg_context: MsgContext, spec: MsgSpec, is_numpy: bool = ...
) -> Iterator[str]: ...
def deserialize_fn_generator(
    msg_context: MsgContext, spec: MsgSpec, is_numpy: bool = ...
) -> Iterator[str]: ...
def msg_generator(
    msg_context: MsgContext, spec: MsgSpec, search_path: Dict[str, List[str]]
) -> Iterator[str]: ...
def srv_generator(
    msg_context: MsgContext, spec: MsgSpec, search_path: Dict[str, List[str]]
) -> Iterator[str]: ...
def compute_resource_name(filename: str, ext: str) -> str: ...
def compute_outfile_name(outdir: str, infile_name: str, ext: str) -> str: ...

class Generator:
    what: str = ...
    ext: str = ...
    spec_loader_fn: Callable[[MsgContext, str, str], MsgSpec] = ...
    generator_fn: Callable[
        [MsgContext, MsgSpec, Dict[str, List[str]]], Iterator[str]
    ] = ...
    def __init__(
        self,
        what: str,
        ext: str,
        spec_loader_fn: Callable[[MsgContext, str, str], MsgSpec],
        generator_fn: Callable[
            [MsgContext, MsgSpec, Dict[str, List[str]]], Iterator[str]
        ],
    ) -> None: ...
    def generate(
        self,
        msg_context: MsgContext,
        full_type: str,
        f: str,
        outdir: str,
        search_path: Dict[str, List[str]],
    ) -> str: ...
    def generate_messages(
        self,
        package: str,
        package_files: Sequence[str],
        outdir: str,
        search_path: Dict[str, List[str]],
    ) -> int: ...

class SrvGenerator(Generator):
    def __init__(self) -> None: ...

class MsgGenerator(Generator):
    def __init__(self) -> None: ...

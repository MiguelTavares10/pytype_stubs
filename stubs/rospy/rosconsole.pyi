from typing import Any, Dict, Iterable, Optional

NAME: str

def error(status: int, msg: str) -> None: ...

class RosConsoleEcho:
    LEVEL_COLOR: Dict[str, int] = ...
    LEVEL_MAX_LENGTH: int = ...
    def __init__(self, options: Any) -> None: ...
    @staticmethod
    def get_levels() -> Iterable[str]: ...

def main(argv: Optional[Any] = ...) -> None: ...

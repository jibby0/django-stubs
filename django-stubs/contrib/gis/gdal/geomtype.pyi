from typing import Any

class OGRGeomType:
    wkb25bit: int
    num: Any
    def __init__(self, type_input: Any) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def name(self) -> Any: ...
    @property
    def django(self) -> Any: ...
    def to_multi(self) -> None: ...

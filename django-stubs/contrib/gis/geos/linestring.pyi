from collections.abc import Iterator
from typing import Any

from django.contrib.gis.geos.geometry import GEOSGeometry as GEOSGeometry
from django.contrib.gis.geos.geometry import LinearGeometryMixin as LinearGeometryMixin

class LineString(LinearGeometryMixin, GEOSGeometry):
    has_cs: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __len__(self) -> int: ...
    @property
    def tuple(self) -> Any: ...
    coords: Any
    @property
    def array(self) -> Any: ...
    @property
    def x(self) -> Any: ...
    @property
    def y(self) -> Any: ...
    @property
    def z(self) -> Any: ...

class LinearRing(LineString):
    @property
    def is_counterclockwise(self) -> Any: ...

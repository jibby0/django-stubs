from typing import Any

GEOIP_SETTINGS: Any

class GeoIP2Exception(Exception): ...

class GeoIP2:
    MODE_AUTO: int
    MODE_MMAP_EXT: int
    MODE_MMAP: int
    MODE_FILE: int
    MODE_MEMORY: int
    cache_options: Any
    def __init__(
        self, path: Any | None = ..., cache: int = ..., country: Any | None = ..., city: Any | None = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def city(self, query: Any) -> Any: ...
    def country_code(self, query: Any) -> Any: ...
    def country_name(self, query: Any) -> Any: ...
    def country(self, query: Any) -> Any: ...
    def coords(self, query: Any, ordering: Any = ...) -> Any: ...
    def lon_lat(self, query: Any) -> Any: ...
    def lat_lon(self, query: Any) -> Any: ...
    def geos(self, query: Any) -> Any: ...
    @property
    def info(self) -> Any: ...
    @classmethod
    def open(cls, full_path: Any, cache: Any) -> Any: ...

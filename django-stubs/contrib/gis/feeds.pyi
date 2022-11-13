from typing import Any

from django.contrib.syndication.views import Feed as BaseFeed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

class GeoFeedMixin:
    def georss_coords(self, coords: Any) -> Any: ...
    def add_georss_point(self, handler: Any, coords: Any, w3c_geo: bool = ...) -> None: ...
    def add_georss_element(self, handler: Any, item: Any, w3c_geo: bool = ...) -> None: ...

class GeoRSSFeed(Rss201rev2Feed, GeoFeedMixin):
    def rss_attributes(self) -> Any: ...
    def add_item_elements(self, handler: Any, item: Any) -> None: ...
    def add_root_elements(self, handler: Any) -> None: ...

class GeoAtom1Feed(Atom1Feed, GeoFeedMixin):
    def root_attributes(self) -> Any: ...
    def add_item_elements(self, handler: Any, item: Any) -> None: ...
    def add_root_elements(self, handler: Any) -> None: ...

class W3CGeoFeed(Rss201rev2Feed, GeoFeedMixin):
    def rss_attributes(self) -> Any: ...
    def add_item_elements(self, handler: Any, item: Any) -> None: ...
    def add_root_elements(self, handler: Any) -> None: ...

class Feed(BaseFeed):
    feed_type: Any
    def feed_extra_kwargs(self, obj: Any) -> Any: ...
    def item_extra_kwargs(self, item: Any) -> Any: ...

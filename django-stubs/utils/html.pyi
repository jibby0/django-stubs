from collections.abc import Iterable
from html.parser import HTMLParser
from re import Pattern
from typing import Any

from django.utils.safestring import SafeString

TRAILING_PUNCTUATION_CHARS: str
WRAPPING_PUNCTUATION: list[tuple[str, str]]
DOTS: list[str]
word_split_re: Pattern[str]
simple_url_re: Pattern[str]
simple_url_2_re: Pattern[str]

def escape(text: Any) -> SafeString: ...
def escapejs(value: Any) -> SafeString: ...
def json_script(value: Any, element_id: str) -> SafeString: ...
def conditional_escape(text: Any) -> str: ...
def format_html(format_string: str, *args: Any, **kwargs: Any) -> SafeString: ...
def format_html_join(sep: str, format_string: str, args_generator: Iterable[Iterable[Any]]) -> SafeString: ...
def linebreaks(value: Any, autoescape: bool = ...) -> str: ...

class MLStripper(HTMLParser):
    fed: Any
    def __init__(self) -> None: ...
    def handle_data(self, d: str) -> None: ...
    def handle_entityref(self, name: str) -> None: ...
    def handle_charref(self, name: str) -> None: ...
    def get_data(self) -> str: ...

def strip_tags(value: str) -> str: ...
def strip_spaces_between_tags(value: str) -> str: ...
def smart_urlquote(url: str) -> str: ...
def urlize(text: str, trim_url_limit: int | None = ..., nofollow: bool = ..., autoescape: bool = ...) -> str: ...
def avoid_wrapping(value: str) -> str: ...
def html_safe(klass: type) -> type: ...

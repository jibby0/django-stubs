from collections.abc import Sequence
from typing import Any

from django.apps.config import AppConfig
from django.core.checks.messages import CheckMessage, Error, Warning
from django.urls import _AnyURL

def check_url_config(app_configs: Sequence[AppConfig] | None, **kwargs: Any) -> Sequence[CheckMessage]: ...
def check_resolver(resolver: _AnyURL) -> Sequence[CheckMessage]: ...
def check_url_namespaces_unique(app_configs: Sequence[AppConfig] | None, **kwargs: Any) -> Sequence[Warning]: ...
def get_warning_for_invalid_pattern(pattern: Any) -> Sequence[Error]: ...
def check_url_settings(app_configs: Sequence[AppConfig] | None, **kwargs: Any) -> Sequence[Error]: ...
def E006(name: str) -> Error: ...

from typing import Any

from django.apps import AppConfig as AppConfig

class GISConfig(AppConfig):
    name: str
    verbose_name: Any
    def ready(self) -> None: ...

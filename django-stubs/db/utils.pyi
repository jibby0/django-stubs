from collections.abc import Iterable
from types import TracebackType
from typing import Any

from django.apps import AppConfig
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Model
from django.utils.connection import BaseConnectionHandler
from django.utils.connection import ConnectionDoesNotExist as ConnectionDoesNotExist

DEFAULT_DB_ALIAS: str
DJANGO_VERSION_PICKLE_KEY: str

class Error(Exception): ...
class InterfaceError(Error): ...
class DatabaseError(Error): ...
class DataError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InternalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...

class DatabaseErrorWrapper:
    def __init__(self, wrapper: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

def load_backend(backend_name: str) -> Any: ...

class ConnectionHandler(BaseConnectionHandler[BaseDatabaseWrapper]):
    @property
    def databases(self) -> dict[str, dict[str, Any]]: ...
    def ensure_defaults(self, alias: str) -> None: ...
    def prepare_test_settings(self, alias: str) -> None: ...
    def create_connection(self, alias: str) -> BaseDatabaseWrapper: ...
    def close_all(self) -> None: ...

class ConnectionRouter:
    def __init__(self, routers: Iterable[Any] | None = ...) -> None: ...
    @property
    def routers(self) -> list[Any]: ...
    def db_for_read(self, model: type[Model], **hints: Any) -> str: ...
    def db_for_write(self, model: type[Model], **hints: Any) -> str: ...
    def allow_relation(self, obj1: Model, obj2: Model, **hints: Any) -> bool: ...
    def allow_migrate(self, db: str, app_label: str, **hints: Any) -> bool: ...
    def allow_migrate_model(self, db: str, model: type[Model]) -> bool: ...
    def get_migratable_models(
        self, app_config: AppConfig, db: str, include_auto_created: bool = ...
    ) -> list[type[Model]]: ...

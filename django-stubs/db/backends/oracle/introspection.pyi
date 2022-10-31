from typing import Any

from django.db.backends.base.introspection import BaseDatabaseIntrospection as BaseDatabaseIntrospection
from django.db.backends.oracle.base import DatabaseWrapper

FieldInfo: Any

class DatabaseIntrospection(BaseDatabaseIntrospection):
    connection: DatabaseWrapper
    cache_bust_counter: int = ...
    @property
    def data_types_reverse(self) -> Any: ...
    def get_field_type(self, data_type: Any, description: Any) -> Any: ...
    def get_table_list(self, cursor: Any) -> Any: ...
    def get_table_description(self, cursor: Any, table_name: Any) -> Any: ...
    def identifier_converter(self, name: Any) -> Any: ...
    def get_sequences(self, cursor: Any, table_name: Any, table_fields: Any = ...) -> Any: ...
    def get_relations(self, cursor: Any, table_name: Any) -> Any: ...
    def get_key_columns(self, cursor: Any, table_name: Any) -> Any: ...
    def get_primary_key_column(self, cursor: Any, table_name: Any) -> Any: ...
    def get_constraints(self, cursor: Any, table_name: Any) -> Any: ...

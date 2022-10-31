from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.operations.base import Operation
from django.db.models.base import Model
from django.db.models.constraints import BaseConstraint
from django.db.models.fields import Field
from django.db.models.indexes import Index
from django.db.models.manager import Manager
from django.db.models.options import _OptionTogetherT

class ModelOperation(Operation):
    name: str = ...
    def __init__(self, name: str) -> None: ...
    @property
    def name_lower(self) -> str: ...

class CreateModel(ModelOperation):
    fields: List[Tuple[str, Field]] = ...
    options: Dict[str, Any] = ...
    bases: Optional[Sequence[Union[Type[Model], str]]] = ...
    managers: Optional[Sequence[Tuple[str, Manager]]] = ...
    def __init__(
        self,
        name: str,
        fields: List[Tuple[str, Field]],
        options: Optional[Dict[str, Any]] = ...,
        bases: Optional[Sequence[Union[Type[Model], str]]] = ...,
        managers: Optional[Sequence[Tuple[str, Manager]]] = ...,
    ) -> None: ...

class DeleteModel(ModelOperation): ...

class RenameModel(ModelOperation):
    old_name: str = ...
    new_name: str = ...
    def __init__(self, old_name: str, new_name: str) -> None: ...
    @property
    def old_name_lower(self) -> str: ...
    @property
    def new_name_lower(self) -> str: ...

class ModelOptionOperation(ModelOperation): ...

class AlterModelTable(ModelOptionOperation):
    table: Optional[str] = ...
    def __init__(self, name: str, table: Optional[str]) -> None: ...

class AlterTogetherOptionOperation(ModelOptionOperation):
    option_name: str = ...
    def __init__(
        self,
        name: str,
        option_value: Optional[_OptionTogetherT],
    ) -> None: ...
    @property
    def option_value(self) -> Optional[Set[Tuple[str, ...]]]: ...
    def deconstruct(self) -> Tuple[str, Sequence[Any], Dict[str, Any]]: ...
    def state_forwards(self, app_label: str, state: Any) -> None: ...
    def database_forwards(
        self, app_label: str, schema_editor: BaseDatabaseSchemaEditor, from_state: Any, to_state: Any
    ) -> None: ...
    def database_backwards(
        self, app_label: str, schema_editor: BaseDatabaseSchemaEditor, from_state: Any, to_state: Any
    ) -> None: ...
    def references_field(self, model_name: str, name: str, app_label: str) -> bool: ...
    def describe(self) -> str: ...
    @property
    def migration_name_fragment(self) -> str: ...

class AlterUniqueTogether(AlterTogetherOptionOperation):
    option_name: str = ...
    unique_together: Optional[Set[Tuple[str, ...]]] = ...
    def __init__(self, name: str, unique_together: Optional[_OptionTogetherT]) -> None: ...

class AlterIndexTogether(AlterTogetherOptionOperation):
    option_name: str = ...
    index_together: Optional[Set[Tuple[str, ...]]] = ...
    def __init__(self, name: str, index_together: Optional[_OptionTogetherT]) -> None: ...

class AlterOrderWithRespectTo(ModelOptionOperation):
    order_with_respect_to: str = ...
    def __init__(self, name: str, order_with_respect_to: str) -> None: ...

class AlterModelOptions(ModelOptionOperation):
    ALTER_OPTION_KEYS: List[str] = ...
    options: Dict[str, Any] = ...
    def __init__(self, name: str, options: Dict[str, Any]) -> None: ...

class AlterModelManagers(ModelOptionOperation):
    managers: Sequence[Tuple[str, Manager]] = ...
    def __init__(self, name: str, managers: Sequence[Tuple[str, Manager]]) -> None: ...

class IndexOperation(Operation):
    option_name: str = ...
    @property
    def model_name_lower(self) -> str: ...

class AddIndex(IndexOperation):
    model_name: str = ...
    index: Index = ...
    def __init__(self, model_name: str, index: Index) -> None: ...

class RemoveIndex(IndexOperation):
    model_name: str = ...
    name: str = ...
    def __init__(self, model_name: str, name: str) -> None: ...

class AddConstraint(IndexOperation):
    def __init__(self, model_name: str, constraint: BaseConstraint) -> None: ...

class RemoveConstraint(IndexOperation):
    def __init__(self, model_name: str, name: str) -> None: ...

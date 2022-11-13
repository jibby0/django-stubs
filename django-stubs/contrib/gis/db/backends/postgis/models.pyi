from typing import Any

from django.contrib.gis.db.backends.base.models import SpatialRefSysMixin as SpatialRefSysMixin
from django.db import models as models

class PostGISGeometryColumns(models.Model):
    f_table_catalog: Any
    f_table_schema: Any
    f_table_name: Any
    f_geometry_column: Any
    coord_dimension: Any
    srid: Any
    type: Any

    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @classmethod
    def table_name_col(cls) -> Any: ...
    @classmethod
    def geom_col_name(cls) -> Any: ...

class PostGISSpatialRefSys(models.Model, SpatialRefSysMixin):
    srid: Any
    auth_name: Any
    auth_srid: Any
    srtext: Any
    proj4text: Any

    class Meta:
        app_label: str
        db_table: str
        managed: bool
    @property
    def wkt(self) -> Any: ...

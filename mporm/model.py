from mporm.fields import TimeField
from mporm.expr import Expr


class Model:

    created_at = TimeField(default="NOW()", not_null=True)
    updated_at = TimeField(default=None, auto_update=True)

    @classmethod
    def where(cls, **kwargs):
        pass

    @classmethod
    def add(cls, **kwargs):
        return Expr(cls, **kwargs).insert()

    @classmethod
    def new(cls, **kwargs):
        pass

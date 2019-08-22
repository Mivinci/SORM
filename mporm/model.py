from mporm.fields import TimeField, StrField
from mporm.expr import Expr


class Model:

    id = StrField(capacity=32, not_null=True)
    created_at = TimeField(default="NOW()", not_null=True)
    updated_at = TimeField(default=None, auto_update=True)

    @classmethod
    def where(cls, **kwargs):
        return Expr(cls, **kwargs).operator

    @classmethod
    def add(cls, **kwargs):
        return Expr(cls, **kwargs).operator.insert()

    @classmethod
    def new(cls, **kwargs):
        return Expr(cls, **kwargs)

    @classmethod
    def drop(cls):
        return Expr(cls).operator.drop()

    @classmethod
    def create(cls):
        return Expr(cls).operator.create()

    @classmethod
    def first(cls):
        pass

    @classmethod
    def last(cls):
        pass

from mporm.fields import TimeField, StrField
from mporm.expr import Expr


field_name_created_at = "created_at"


class Model:

    id = StrField(capacity=32, default="replace(uuid(), '-', '')", not_null=True)
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
    def first(cls, num: int = 0):
        if num == 0:
            return Expr(cls).operator.order(field_name_created_at).findone()
        else:
            return Expr(cls).operator.order(field_name_created_at).limit(num).find()

    @classmethod
    def last(cls, num: int = 0):
        if num == 0:
            return Expr(cls).operator.order(field_name_created_at, desc=True).findone()
        else:
            return Expr(cls).operator.order(field_name_created_at, desc=True).limit(num).find()

    @classmethod
    def take(cls, num: int = 0):
        if num == 0:
            return Expr(cls).operator.findone()
        else:
            return Expr(cls).operator.limit(num).find()

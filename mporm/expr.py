from mporm.dsn import DSN
from mporm.fields import Field
from mporm.oper import Operator

from mporm.orm import ORM


# You can't import `mporm.schema` in this file!!

__dsn__ = "__dsn__"
__prefix__ = "__prefix__"


class Expr:
    def __init__(self, model, **kwargs):
        self.params:   dict = kwargs
        self.reflect:  dict = model.__dict__
        self.md_name:   str = model.__name__.lower()
        self.dsn:       DSN = self.reflect.get(__dsn__) or ORM.dsn
        self.tb_prefix: str = self.reflect.get(__prefix__)
        self.tb_name:   str = self.md_name if not self.tb_prefix else f"{self.tb_prefix.lower()}_{self.md_name}"

        self.fields: [tuple] = [(k, v.__dict__) for k, v in self.reflect.items() if isinstance(v, Field)]

    def operator(self):
        return Operator(self)

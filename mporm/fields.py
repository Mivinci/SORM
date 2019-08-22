class Field:
    def __init__(self, default=None, not_null=False):
        self.default = default
        self.not_null = not_null


class StrField(Field):
    def __init__(self,
                 capacity: int = 255,
                 default: str = None,
                 not_null: bool = False):
        super().__init__(default, not_null)
        self.type = "VARCHAR"
        self.capacity = capacity


class IntField(Field):
    def __init__(self,
                 size: int = 11,
                 default: int = None,
                 not_null: bool = False):
        super().__init__(default, not_null)
        self.type = "INT"
        self.size = size


class TimeField(Field):
    def __init__(self,
                 default: str = None,
                 not_null: bool = False,
                 auto_update: bool = False):
        super().__init__(default, not_null)
        self.type = "TIMESTAMP"
        self.auto_update = auto_update


class BoolField(IntField):
    def __init__(self,
                 default: bool = False,
                 not_null=True):
        super().__init__(size=1,
                         default=1 if default else 0,
                         not_null=not_null)


class FloatField(Field):
    def __init__(self,
                 size: int = 32,
                 default: float = None,
                 not_null: bool = False):
        super().__init__(default, not_null)
        self.type = "double" if size == 64 else "float"
        self.size = size

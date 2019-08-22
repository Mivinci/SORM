from mporm.fields import Field
from mporm.operator import Operator


class Expr:
    def __init__(self, model, **kwargs):
        self.params:   dict = kwargs
        self.reflect:  dict = model.__dict__
        self.md_name:   str = model.__name__.lower()
        self.tb_prefix: str = self.reflect.get("__prefix__")
        self.tb_name:   str = self.md_name if not self.tb_prefix else f"{self.tb_prefix.lower()}_{self.md_name}"

        self.fields: [tuple] = [(k, v.__dict__) for k, v in self.reflect.items() if isinstance(v, Field)]

        self.required: tuple = ()

    # Creates new table
    def create(self) -> bool:
        pass

    # Drops a specified table
    def drop(self) -> bool:
        pass

    # Inserts a new row to the specified table
    def insert(self) -> bool:
        pass

    def operator(self):
        return Operator(self)

from mporm.executor import Executor


# You can't import `mporm.schema` in this file!!


class Operator:

    # limit_value: int
    # offset_value: int

    def __init__(self, expr):
        self.expr = expr

        self.order_field = None
        self.order_desc = False
        self.offset_value = None
        self.limit_value = None
        self.require_fields = ()
        self.update_values = {}

        self.executor = Executor(expr, self)

    # Creates a new table
    def create(self):
        return self.executor.create()

    # Drops a specified table
    def drop(self):
        return self.executor.drop()

    # The 4 + 1 Functions below are what we call 'CRUD'

    def insert(self):
        return self.executor.insert()

    def delete(self) -> int:
        return self.executor.delete()

    def update(self) -> int:
        return Executor(self.expr, self).update()

    def find(self) -> list:
        return Executor(self.expr, self).select()

    def findone(self) -> dict:
        return Executor(self.expr, self).select_one()

    # Functions below return `self` since they're used to build chains

    def filter(self, *args):
        return self.select(*args).find()

    def select(self, *args):
        self.require_fields = args
        return self

    """
    Can be followed by method
        `self.update`.
    """
    def set(self, **kwargs):
        self.update_values = kwargs
        return self

    """
    Can be followed by method 
        self.find, self.offset, self.limit.
    """
    def order(self,
              field: str,
              desc: bool = False):
        self.order_field = field
        self.order_desc = desc
        return self

    """
    Can be followed by method 
        self.find, self.limit.
    """
    def offset(self, offset: int):
        self.offset_value = offset
        return self

    """
    Can be followed by method 
        self.find, 
    """
    def limit(self, limit: int):
        self.limit_value = limit
        return self

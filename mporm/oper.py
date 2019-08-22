from mporm.executor import Executor


# You can't import `mporm.schema` in this file!!


class Operator:

    def __init__(self, expr):
        self.expr = expr

        self.order_field = None
        self.order_desc = False
        self.offset = None
        self.limit = None
        self.require_fields = ()
        self.update_values = {}

        self.executor = Executor(expr, self)

    # Creates a new table
    def create(self) -> bool:
        return self.executor.create()

    # Drops a specified table
    def drop(self) -> bool:
        return self.executor.drop()

    # The 4 Functions below are what we call 'CRUD'

    def insert(self) -> bool:
        return self.executor.insert()

    def delete(self) -> bool:
        return self.executor.delete()

    def update(self) -> bool:
        return Executor(self.expr, self).update()

    def find(self) -> int:
        return Executor(self.expr, self).select()

    # Functions below return `self` since they're used to build chains

    def filter(self, *args) -> int:
        return self.require(*args).find()

    # Followed by `self.find`.
    def require(self, *args):
        self.require_fields = args
        return self

    """
    Can't be followed by method
        `self.update`.
    """
    def values(self, **kwargs):
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
        self.offset = offset
        return self

    """
    Can be followed by method 
        self.find, 
    """
    def limit(self, limit: int):
        self.limit = limit
        return self

from mporm.executor import Executor


# You can't import `mporm.schema` in this file!!


class Operator:

    def __init__(self, expr):
        self.expr = expr
        self.require_fields = ()
        self.order_field = None
        self.order_desc = False
        self.offset = None
        self.limit = None

        self.executor = Executor(expr, self)

    # Creates a new table
    def create(self) -> bool:
        return self.executor.create()

    # Drops a specified table
    def drop(self) -> bool:
        return self.executor.drop()

    # The 4 Functions below are what we call 'CRUD'

    def insert(self) -> bool:
        pass

    def delete(self) -> bool:
        pass

    def update(self) -> bool:
        pass

    def find(self) -> int:
        print(self.require_fields)
        return 1

    # Functions below return `self` since they're used to build chains

    def filter(self, *args) -> int:
        return self.require(*args).find()

    def require(self, *args):
        self.require_fields = args
        return self

    def order(self,
              field: str,
              desc: bool = False):
        self.order_field = field
        self.order_desc = desc
        return self

    def offset(self, offset: int):
        self.offset = offset
        return self

    def limit(self, limit: int):
        self.limit = limit
        return self

# You can't import `mporm.schema` in this file!!


class Operator:
    def __init__(self, expr):
        self._expr = expr
        self._require_fields = ()
        self._order_field = None
        self._order_desc = False
        self._offset = None
        self._limit = None

    # Creates a new table
    def create(self) -> bool:
        pass

    # Drops a specified table
    def drop(self) -> bool:
        pass

    # The 4 Functions below are what we call 'CRUD'

    def insert(self) -> bool:
        pass

    def delete(self) -> bool:
        pass

    def update(self) -> bool:
        pass

    def find(self) -> int:
        print(self._require_fields)
        return 1

    # Functions below return `self` since they're used to build chains

    def filter(self, *args) -> int:
        return self.require(*args).find()

    def require(self, *args):
        self._require_fields = args
        return self

    def order(self,
              field: str,
              desc: bool = False):
        self._order_field = field
        self._order_desc = desc
        return self

    def offset(self, offset: int):
        self._offset = offset
        return self

    def limit(self, limit: int):
        self._limit = limit
        return self

from mporm.schema import Schema
from mporm.sql import SingleSQL


class Executor:
    def __init__(self, expr, oper):
        self.expr = expr
        self.oper = oper
        self.schema = Schema(expr, oper)

    def create(self):
        if not self.expr.dsn:
            SingleSQL.execute(self.schema.create())
        else:
            pass

    def drop(self):
        SingleSQL.execute(self.schema.drop())

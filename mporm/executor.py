from mporm.schema import Schema
from mporm.sql import SingleSQL


class Executor:
    def __init__(self, expr, oper):
        self.expr = expr
        self.oper = oper
        self.schema = Schema(expr, oper)

    def create(self):
        sql = self.schema.create()
        if not self.expr.dsn:
            try:
                SingleSQL.execute(sql)
            except Exception as err:
                print(err)
        else:
            pass

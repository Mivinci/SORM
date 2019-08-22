from mporm.schema import Schema
from mporm.sql import SingleSQL, SQL


class Executor:
    def __init__(self, expr, oper):
        self.expr = expr
        self.oper = oper
        self.schema = Schema(expr, oper)

        if expr.dsn:
            self.sql = SQL(expr.dsn)

    def create(self):
        sql: str = self.schema.create()
        if not self.expr.dsn:
            # print(sql)
            SingleSQL.execute(sql)
        else:
            self.sql.execute(sql)

    def drop(self):
        sql: str = self.schema.drop()
        if not self.expr.dsn:
            SingleSQL.execute(sql)
        else:
            self.sql.execute(sql)

    def insert(self):
        sql:   str = self.schema.insert()
        value: tuple = tuple(self.expr.params.values())
        if not self.expr.dsn:
            SingleSQL.execute(sql, value)
        else:
            self.sql.execute(sql, value)

    def delete(self):
        pass

    def update(self):
        pass

    def select(self):
        pass

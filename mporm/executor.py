from mporm.schema import Schema
from mporm.sql import SingleSQL, SQL


class Executor:
    def __init__(self, expr, oper):
        self.expr = expr
        self.oper = oper
        self.schema = Schema(expr, oper)

        self.where_expression_values = tuple(expr.params.values())
        self.update_params_values = tuple(oper.update_values.values())

        if expr.dsn:
            self.sql = SQL(expr.dsn)

    def create(self) -> int:
        sql: str = self.schema.create()
        if not self.expr.dsn:
            SingleSQL.execute(sql)
            return SingleSQL.affected
        else:
            self.sql.execute(sql)
            return self.sql.affected

    def drop(self) -> int:
        sql: str = self.schema.drop()
        if not self.expr.dsn:
            SingleSQL.execute(sql)
            return SingleSQL.affected
        else:
            self.sql.execute(sql)
            return self.sql.affected

    def insert(self) -> int:
        sql:   str = self.schema.insert()
        if not self.expr.dsn:
            SingleSQL.execute(sql, self.where_expression_values)
            return SingleSQL.affected
        else:
            self.sql.execute(sql, self.where_expression_values)
            return self.sql.affected

    def delete(self) -> int:
        sql: str = self.schema.delete()
        if not self.expr.dsn:
            print(sql)
            SingleSQL.execute(sql, self.where_expression_values)
            return SingleSQL.affected
        else:
            self.sql.execute(sql, self.where_expression_values)
            return self.sql.affected

    def update(self) -> int:
        sql: str = self.schema.update()
        if not self.expr.dsn:
            SingleSQL.execute(sql, self.update_params_values + self.where_expression_values)
            return SingleSQL.affected
        else:
            self.sql.execute(sql, self.update_params_values + self.where_expression_values)
            return self.sql.affected

    def select(self):
        sql: str = self.schema.select()
        if not self.expr.dsn:
            return SingleSQL.execute(sql, self.where_expression_values).fetchall()
        else:
            return self.sql.execute(sql, self.where_expression_values).fetchall()

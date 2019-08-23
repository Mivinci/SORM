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
        return Affect.execute(sql, self)

    def drop(self) -> int:
        sql: str = self.schema.drop()
        return Affect.execute(sql, self)

    def insert(self) -> int:
        sql:   str = self.schema.insert()
        return Affect.execute(sql, self, self.where_expression_values)

    def delete(self) -> int:
        sql: str = self.schema.delete()
        return Affect.execute(sql, self, self.where_expression_values)

    def update(self) -> int:
        sql: str = self.schema.update()
        return Affect.execute(sql, self, self.update_params_values + self.where_expression_values)

    def select(self) -> list:
        sql: str = self.schema.select()
        return Query.fetchall(sql, self)

    def select_one(self) -> dict:
        sql: str = self.schema.select()
        return Query.fetchone(sql, self)

    def count(self, field: str) -> int:
        sql: str = self.schema.count(field)
        return Query.fetchone(sql, self)[f"count({field})"]


class Query:

    @classmethod
    def fetchall(cls, sql: str, executor: Executor) -> list:
        if not executor.expr.dsn:
            return SingleSQL.execute(sql, executor.where_expression_values).fetchall()
        else:
            return executor.sql.execute(sql, executor.where_expression_values).fetchall()

    @classmethod
    def fetchone(cls, sql: str, executor: Executor) -> dict:
        if not executor.expr.dsn:
            return SingleSQL.execute(sql, executor.where_expression_values).fetchone()
        else:
            return executor.sql.execute(sql, executor.where_expression_values).fetchone()


class Affect:

    @classmethod
    def execute(cls, sql: str, executor: Executor, args: tuple = None) -> int:
        if not executor.expr.dsn:
            SingleSQL.execute(sql, args)
            return SingleSQL.affected
        else:
            executor.sql.execute(sql, args)
            return executor.sql.affected

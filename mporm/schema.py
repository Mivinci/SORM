from typing import Callable

from mporm.operator import Operator
from mporm.expr import Expr

tb_drop: Callable[[str], str] = lambda tb_name: f"drop table {tb_name};"


# tb_create: Callable[[Any], str] = lambda


class Schema:
    def __init__(self, expr, operator=None):
        self._expr: Expr = expr
        self._oper: Operator = operator
        print(self._expr.fields)

    def create(self) -> str:
        pass

    def drop(self) -> str:
        return tb_drop(self._expr.tb_name)

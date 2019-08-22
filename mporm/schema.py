from mporm.convert import TYPE_STR, TYPE_INT, TYPE_BOOL, TYPE_FLOAT32, TYPE_FLOAT64, TYPE_TIME
from mporm.convert import Convert, iDESC, iNAME

from typing import Callable


tb_drop: Callable[[str], str] = lambda tb_name: f"drop table {tb_name};"


_iNAME = iNAME
_iDESC = iDESC
_key_t = "type"


def spread_tb_fields(fields: list):
    for field in fields:
        field_type: str = field[_iDESC][_key_t]
        if field_type == TYPE_STR:
            yield Convert.str(field)
        elif field_type == TYPE_INT:
            yield Convert.int(field)
        elif field_type == TYPE_TIME:
            yield Convert.time(field)
        elif field_type == TYPE_BOOL:
            yield Convert.bool(field)
        elif field_type == TYPE_FLOAT32 or field_type == TYPE_FLOAT64:
            yield Convert.float(field)
        else:
            yield ""


tb_create: Callable[[str, list], str] = lambda tb_name, tb_fields: \
    f"create table if not exists `{tb_name}` (" \
    f"{', '.join(spread_tb_fields(tb_fields))}" \
    f") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"


class Schema:
    def __init__(self, expr, operator=None):
        self._expr = expr
        self._oper = operator

    def create(self) -> str:
        return tb_create(self._expr.tb_name, self._expr.fields)

    def drop(self) -> str:
        return tb_drop(self._expr.tb_name)

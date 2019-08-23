from mporm.convert import TYPE_STR, TYPE_INT, TYPE_BOOL, TYPE_FLOAT32, TYPE_FLOAT64, TYPE_TIME
from mporm.convert import Convert, iDESC, iNAME

from typing import Callable

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


def spread_where_expression(expression: dict):
    for k, _ in expression.items():
        yield f"{k} = %s"


def spread_new_values(values: dict):
    for k, _ in values.items():
        yield f"{k} = %s"


def consist_order_expression(order_field: str, order_desc: bool) -> str:
    return f"""{f"order by {order_field} {'desc' if order_desc else 'asc'}" if order_field else ""}"""


consist_offset_expression: Callable[[int], str] = lambda offset: \
    f"""{f"offset {offset}" if isinstance(offset, int) else ""}"""

consist_limit_expression: Callable[[int], str] = lambda limit: \
    f"""{f"limit {limit}" if isinstance(limit, int) else ""}"""

# The ugly functions below are used to construct sql statement


tb_create: Callable[[str, list], str] = lambda tb_name, tb_fields: \
    f"create table if not exists `{tb_name}` (" \
    f"{', '.join(spread_tb_fields(tb_fields))}" \
    f") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

tb_drop: Callable[[str], str] = lambda tb_name: f"drop table {tb_name};"

row_insert: Callable[[str, dict], str] = lambda tb_name, params: \
    f"insert into {tb_name} ({', '.join(params.keys())}) values" \
    f" ({', '.join(['%s' for _ in range(params.__len__())])});"

row_delete: Callable[[str, dict], str] = lambda tb_name, where_expression: \
    f"delete from {tb_name} where {' and '.join(spread_where_expression(where_expression))};"


def row_update(tb_name: str, where_expression: dict, new_values: dict) -> str:
    return f"update {tb_name} set" \
           f" {', '.join(spread_new_values(new_values))} where" \
           f" {' and '.join(spread_where_expression(where_expression))};"


def row_select(tb_name: str,
               where_expression: dict,
               require_fields: tuple,
               order_field: str, order_desc: bool,
               offset: int,
               limit: int) -> str:
    return f"select {', '.join(require_fields) or '*'} from {tb_name}" \
           f" {'' if not where_expression else 'where'}" \
           f" {' and '.join(spread_where_expression(where_expression))}" \
           f" {consist_order_expression(order_field, order_desc)}" \
           f" {consist_limit_expression(limit)}" \
           f" {consist_offset_expression(offset)};"


class Schema:
    def __init__(self, expr, operator=None):
        self._expr = expr
        self._oper = operator

    def create(self) -> str:
        return tb_create(self._expr.tb_name, self._expr.fields)

    def drop(self) -> str:
        return tb_drop(self._expr.tb_name)

    def insert(self) -> str:
        return row_insert(self._expr.tb_name, self._expr.params)

    def delete(self) -> str:
        return row_delete(self._expr.tb_name, self._expr.params)

    def update(self) -> str:
        return row_update(self._expr.tb_name, self._expr.params, self._oper.update_values)

    def select(self) -> str:
        return row_select(self._expr.tb_name,
                          self._expr.params,
                          self._oper.require_fields,
                          self._oper.order_field, self._oper.order_desc,
                          self._oper.offset_value,
                          self._oper.limit_value)

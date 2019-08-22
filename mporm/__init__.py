from mporm.operator import Operator
from mporm.schema import Schema
from mporm.model import Model
from mporm.expr import Expr
from mporm.fields import *

from typing import TypedDict


class DSN(TypedDict):
    def __init__(self):
        pass

    user: str
    password: str
    host: str
    port: int
    database: str
    charset: str


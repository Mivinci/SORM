from typing import Union

from pymysql.cursors import Cursor

from mporm.dsn import DSN

"""
    orm = ORM.load(DSN(user="", password="", ...))
"""


class ORM:
    dsn: DSN = None

    @classmethod
    def load(cls, dsn: DSN):
        cls.dsn = dsn

    @classmethod
    def load_file(cls, filename: str):
        pass

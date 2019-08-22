from pymysql import Connection, connect, cursors, DatabaseError

from mporm import DSN


class Database:
    connection: Connection = None

    @classmethod
    def open(cls, dsn: DSN) -> Connection:
        if not cls.connection or not cls.connection.open:
            cls.connect(dsn.user, dsn.password, dsn.host, dsn.port, dsn.database, dsn.charset)
        return cls.connection

    @classmethod
    def connect(cls, user: str, password: str, host: str, port: int, database: str,
                charset: str):
        try:
            cls.connection = connect(user=user,
                                     password=password,
                                     host=host,
                                     port=port,
                                     db=database,
                                     charset=charset,
                                     cursorclass=cursors.DictCursor)
        except DatabaseError as de:
            print(de)

    @classmethod
    def execute(cls, sql, *args):
        try:
            with cls.open()


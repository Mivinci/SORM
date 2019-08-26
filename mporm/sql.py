import toml
from pymysql import Connection, connect, cursors, DatabaseError
from pymysql.cursors import Cursor

from mporm.dsn import DSN


class SQL:
    def __init__(self, dsn: DSN):
        self.dsn: DSN = dsn
        self.affected = 0
        self.connection: Connection = None

    def open(self) -> Connection:
        if not self.connection or not self.connection.open:
            self.connection = SingleSQL.connect(
                self.dsn.user,
                self.dsn.password,
                self.dsn.host, self.dsn.port, self.dsn.database, self.dsn.charset)
        return self.connection

    def execute(self, sql: str, args: tuple = None) -> Cursor:
        try:
            with self.open().cursor() as cursor:
                self.affected = cursor.execute(sql, args)
            self.connection.commit()
            return cursor
        except Exception as err:
            self.close()
            raise err
        finally:
            pass

    def close(self):
        self.connection.close()


class SingleSQL:
    connection: Connection = None
    affected = 0

    @classmethod
    def open(cls, dsn: DSN) -> Connection:
        if not cls.connection or not cls.connection.open:
            cls.connection = cls.connect(dsn.user, dsn.password, dsn.host, dsn.port, dsn.database, dsn.charset)
        return cls.connection

    @classmethod
    def connect(cls, user: str, password: str, host: str, port: int, database: str,
                charset: str):
        try:
            return connect(user=user,
                           password=password,
                           host=host,
                           port=port,
                           db=database,
                           charset=charset,
                           cursorclass=cursors.DictCursor)
        except DatabaseError as err:
            print(err)

    @classmethod
    def execute(cls, sql: str, args: tuple = None) -> Cursor:
        try:
            with cls.open(ORM.dsn).cursor() as cursor:
                cls.affected = cursor.execute(sql, args)
            cls.connection.commit()
            return cursor
        except Exception as err:
            cls.close()
            raise err
        finally:
            pass

    @classmethod
    def close(cls):
        cls.connection.close()


class ORM:
    dsn: DSN = None

    @classmethod
    def load(cls, dsn: DSN):
        cls.dsn = dsn

    @classmethod
    def load_file(cls, filename: str, key: str = "database"):
        d: dict = toml.load(filename).get(key)
        cls.dsn = DSN(user=d.get("user"),
                      password=d.get("password"),
                      host=d.get("host"),
                      port=d.get("port"),
                      database=d.get("database"),
                      charset=d.get("charset"))

    @classmethod
    def close(cls):
        SingleSQL.close()

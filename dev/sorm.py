from datetime import datetime
import pymysql


class Field:
    pass


class AutoField(Field):
    pass


class StrField(Field):
    def __init__(self, maxlen, default):
        self.type = 'VARCHAR'
        self.maxlen = maxlen
        self.default = default


class IntField(Field):
    def __init__(self, maxlen, default):
        self.type = 'INT'
        self.maxlen = maxlen
        self.default = default


class DatetimeField(Field):
    def __init__(self):
        self.type = 'DATETIME'
        self.maxlen = 6
        self.default = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Expr:
    def __init__(self, model, **kwargs):
        self.fields = [(key, val.__dict__) for key, val in model.__dict__.items() if isinstance(val, Field)]
        self.table = model.__name__.lower() if not model.__dict__.get('__table__') else model.__dict__.get('__table__')
        self.model = model
        self.params = kwargs

    def select(self):
        pass

    def insert(self):
        pass

    def create(self):
        print(self.fields)
        print(self.table)


class Model:

    @classmethod
    def where(cls, **kwargs):
        return Expr(cls, **kwargs)

    @classmethod
    def new(cls, **kwargs):
        return Expr(cls, **kwargs)

    @classmethod
    def migrate(cls):
        return Expr(cls)


class Database:
    conn = None
    db_config = {}
    auto_commit = True

    @classmethod
    def connect(cls, **kwargs):
        cls.conn = pymysql.connect(
            user=kwargs.get('user'),
            passwd=kwargs.get('password'),
            host=kwargs.get('host'),
            port=int(kwargs.get('port')),
            db=kwargs.get('database'),
            charset=kwargs.get('charset')
        )
        cls.conn.autocommit(cls.auto_commit)
        cls.db_config.update(kwargs)

    @classmethod
    def get_conn(cls):
        if not cls.conn or not cls.conn.open:
            cls.connect(**cls.db_config)
        return cls.conn

    @classmethod
    def execute(cls, sql, *args):
        return cls.get_conn().cursor().execute(sql, args)

    @classmethod
    def get_db_config(cls):
        return cls.db_config

    def __del__(self):
        self.conn.close()



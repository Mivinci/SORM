from dev.sql import Sql
from dev.conf.config import DB_CONFIG
import pymysql


class Field:
    pass


class AutoField(Field):
    pass


class StrField(Field):
    def __init__(self, **kwargs):
        self.type = 'VARCHAR'
        self.maxlen = '255' if not kwargs.get('maxlen') else kwargs.get('maxlen')
        self.default = None if not kwargs.get('default') else kwargs.get('default')


class IntField(Field):
    def __init__(self, **kwargs):
        self.type = 'INT'
        self.maxlen = '11' if not kwargs.get('maxlen') else kwargs.get('maxlen')
        self.default = None if not kwargs.get('default') else kwargs.get('default')


class TimeField(Field):
    def __init__(self, **kwargs):
        self.type = 'TIMESTAMP'
        self.default = 'NOW()' if not kwargs.get('default') else f"""'{kwargs.get('default')}'"""
        self.auto_update = True if 'auto_update' in kwargs.keys() and kwargs.get('auto_update') else False


class Expr:
    def __init__(self, model, **kwargs):
        self.fields = [(key, val.__dict__) for key, val in model.__dict__.items() if isinstance(val, Field)]
        self.table = model.__name__.lower() if not model.__dict__.get('__table__') else model.__dict__.get('__table__')
        self.model = model
        self.params = kwargs
        self.needs = ()

    def create(self):
        sql = Sql.create(self.table, self.fields).sql
        Database.connect(**DB_CONFIG).execute(sql)

    def drop(self):
        Database.connect(**DB_CONFIG).execute(Sql.drop(self.table).sql)

    def select(self):
        sql = Sql.select(self.table, self.needs, self.params).sql
        return tuple_to_list(self.needs if self.needs else (fd[0] for fd in self.fields),
                             Database.connect(**DB_CONFIG).execute(sql).fetchall())

    def need(self, *args):
        self.needs = args
        return self

    def insert(self):
        sql = Sql.insert(self.table, self.params).sql
        Database.connect(**DB_CONFIG).execute(sql)

    def delete(self):
        sql = Sql.delete(self.table, self.params).sql
        Database.connect(**DB_CONFIG).execute(sql)

    def update(self, **kwargs):
        sql = Sql.update(self.table, self.params, kwargs).sql
        Database.connect(**DB_CONFIG).execute(sql)
        print(sql)


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
    db_config = None

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
        cls.conn.autocommit(True)
        cls.db_config = kwargs
        return cls

    @classmethod
    def get_conn(cls):
        if not cls.conn or not cls.conn.open:
            cls.conn = cls.connect(**db_config)
        return cls.conn

    @classmethod
    def execute(cls, sql, *args):
        try:
            with cls.get_conn().cursor() as cursor:
                cursor.execute(sql, args)
                return cursor
        except Exception as e:
            print(e)
        finally:
            cls.conn.close()

    @classmethod
    def close(cls):
        cls.conn.close()

    @classmethod
    def get_db_config(cls):
        return cls.db_config

    def __del__(self):
        self.conn.close()


def tuple_to_list(keys, t):
    res = []
    key_list = [key for key in keys]
    start_i = 1 if 'id' in keys else 0
    for each in t:
        d = {}
        for i, key in enumerate(key_list, start_i):
            d[key] = each[i]
        res.append(d)
    return res

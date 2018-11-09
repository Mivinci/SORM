from .sql import Sql
from tsorm.conf.config import DB_CONFIG
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
        self.db_config = DB_CONFIG if not model.__dict__.get('__db__') else model.__dict__.get('__db__')  # TODO
        self.model = model
        self.params = stringify_dict_values(kwargs)
        self.needs = ()

    def create(self):
        sql = Sql.create(self.table, self.fields).sql
        Database.connect(**self.db_config).execute(sql)
        return Database.affected

    def drop(self):
        Database.connect(**self.db_config).execute(Sql.drop(self.table).sql)
        return Database.affected

    def select(self, fuzzy=False):
        sql = Sql.select(self.table, self.needs, self.params, fuzzy).sql
        return tuple2list(self.needs if self.needs and '*' not in self.needs else (fd[0] for fd in self.fields),
                          Database.connect(**self.db_config).execute(sql).fetchall())

    def need(self, *args):
        self.needs = args
        return self

    def insert(self):
        sql = Sql.insert(self.table, self.params).sql
        Database.connect(**self.db_config).execute(sql)
        return Database.affected

    def delete(self):
        sql = Sql.delete(self.table, self.params).sql
        Database.connect(**self.db_config).execute(sql)
        return Database.affected

    def update(self, **kwargs):
        sql = Sql.update(self.table, self.params, kwargs).sql
        Database.connect(**self.db_config).execute(sql)
        return Database.affected

    def count(self, field):
        return Database.connect(**self.db_config).execute(Sql.count(self.table, field).sql).fetchone()[0]


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
    affected = None
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
            cls.conn = cls.connect(**cls.db_config)
        return cls.conn

    @classmethod
    def execute(cls, sql, *args):
        try:
            with cls.get_conn().cursor() as cursor:
                cls.affected = cursor.execute(sql, args)
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


def tuple2list(keys, t):
    res = []
    key_list = [key for key in keys]
    for each in t:
        d = {}
        for i, key in enumerate(key_list):
            d[key] = each[i] if len(each) == len(key_list) else each[1::][i]
        res.append(d)
    return res


def stringify_dict_values(d: dict):
    for key, val in d.items():
        d[key] = str(val)
    return d

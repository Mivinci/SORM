import pymysql


class Field:
    pass


class Expr:
    def __init__(self, model, **kwargs):
        self.model = model
        # self.params = kwargs.value()
        # equations = [key + ' = %s' for key in kwargs.key()]
        # self.where_expr = 'where ' + ' and '.join(equations) if len(equations) > 0 else ''

    def select(self):
        print(self.model.fields.key())


class MetaModel(type):
    db_table = None
    fields = {}

    def __init__(cls, name, bases, attrs):
        super(MetaModel, cls).__init__(name, bases, attrs)
        fields = {}
        for key, val in cls.__dict__.items():
            if isinstance(key, Field):
                fields[key] = val
        cls.fields = fields
        cls.attrs = attrs


class Model(object):
    __metaclass__ = MetaModel

    # def create(self):
    #     print(self.)

    @classmethod
    def where(cls, **kwargs):
        return Expr(cls, **kwargs)


class User(Model):
    db_table = 'user'
    name = Field()
    age = Field()


# user = User
# user.name = 'Jack'
# user.age = 23
# user.where(name='Jack').select()


class Database:
    autocommit = True
    conn = None
    db_config = {}

    @classmethod
    def connect(cls, **kwargs):
        cls.conn = pymysql.connect(user=kwargs.get('user'), passwd=kwargs.get('passwd'),
                                   host=kwargs.get('host'), port=int(kwargs.get('host')),
                                   db=kwargs.get('db'), charset=kwargs.get('charset'))
        cls.conn.autocommit(cls.autocommit)
        cls.db_config.update(kwargs)

    @classmethod
    def get_conn(cls):
        if not cls.conn or not cls.conn.open:
            cls.connect(**cls.db_config)
        try:
            cls.conn.ping()
        except pymysql.OperationalError:
            cls.connect(**cls.db_config)
        return cls.conn

    @classmethod
    def execute(cls, *args):
        cursor = cls.get_conn().cursor()
        cursor.execute(*args)
        return cursor

    def __del__(self):
        if self.conn and self.conn.open:
            self.conn.close()


def execute_raw_sql(sql, params=None):
    return Database.execute(sql, params) if params else Database.execute(sql)

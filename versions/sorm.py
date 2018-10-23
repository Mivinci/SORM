class Field(object):
    pass


class MetaModel(type):
    def __new__(mcs, name, bases, attrs):
        mapping = ...
        primary_key = ...
        __table__ = mcs.__table__
        attrs['__mapping__'] = mapping
        attrs['__primary_key__'] = primary_key
        attrs['__table__'] = __table__
        return type.__new__(mcs, name, bases, attrs)


class Model(dict):
    __metaclass__ = MetaModel

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def create(self):
        print(self.__dict__)


class User(Model):
    __table__ = 'user'
    name = Field()
    age = Field()


user = User
user.create()



class Field(object):
    pass


class MetaModel(type):
    db_table = None
    fields = {}

    def __init__(cls, name, bases, attrs):
        super(MetaModel, cls).__init__(name, bases, attrs)
        fields = {}
        for key, val in cls.__dict__.items():
            print(key)
            print(val)
            if isinstance(key, val):
                fields[key] = val
        cls.fields = fields
        cls.attrs = attrs


class Model(object):
    __metaclass__ = MetaModel


class User(Model):
    name = Field()
    age = Field()


user = User
# print(user.name)

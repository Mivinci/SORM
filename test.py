from tsorm.dev.orm import Model, StrField, IntField, TimeField

db_config = {
    'user': 'root',
    'password': 'xxxxxx',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'wx',
    'charset': 'utf8'
}


class User(Model):
    __db__ = db_config
    name = StrField(maxlen=25)
    age = IntField(default=23)
    first_time = TimeField(auto_update=True)


# s = User.migrate().create()

# s = User.new(name='Tom', age=19).insert()

# s = User.where(age=18, name='Katherine').delete()

# s = User.where(name='Tom').need('name').select(fuzzy=True)

# s = User.where(name='Ally').update(age=23)

# s = User.migrate().count('name')

# s = User.migrate().drop()


# print(s)


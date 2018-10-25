from dev.sorm import Model, StrField, IntField, TimeField


class User(Model):
    __table__ = 'user_info'
    name = StrField(maxlen=25)
    age = IntField(default=23)
    first_time = TimeField(auto_update=True)


# s = User.migrate().create()

# s = User.new(name='Adam', age=40).insert()

# s = User.where(age=18, name='Katherine').delete()

# s = User.where(age=23).need('name').select()

# s = User.migrate().count('name')

# s = User.migrate().drop()


# print(s)


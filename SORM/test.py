from .dev.sorm import Model, StrField, IntField, TimeField


class User(Model):
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


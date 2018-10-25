from dev.sorm import Model, StrField, IntField, TimeField


class User(Model):
    __table__ = 'user_info'
    name = StrField(maxlen=25)
    age = IntField(default=23)
    first_time = TimeField(auto_update=True)


class Student(Model):
    name = StrField()
    stu_num = StrField()
    class_num = StrField()
    first_time = TimeField()


# User.migrate().create()

# User.new(name='Tom', age=23).insert()

s = User.where(age=18, name='Katherine').delete()

print(s)


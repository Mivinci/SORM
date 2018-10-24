from dev.sorm import Model, StrField, IntField, TimeField, Database
from dev.conf.config import DB_CONFIG


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


# Student.migrate().drop()
# Student.migrate().create()

# Student.new(name='Jack', class_num='2019213056').insert()
# print(Student.where(name='Jack', class_num='2021213056').need('name').select())

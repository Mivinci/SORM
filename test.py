from dev.sorm import Model, StrField, IntField, TimeField, Database


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
Student.migrate().create()

Student.new(name='Jack', stu_num='2019213060').insert()
# Student.where(name='Jack', class_num='2019213056').update(stu_num='2019213056', class_num='08051903')

Student.where(id=4).delete()


# s = Student.where(name='Jack').need('name', 'stu_num').select()
# print(s)

# c = Student.migrate().count('class_num')
# print(c)

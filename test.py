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
# Student.migrate().create()

# Student.new(name='Jack', stu_num='2019213056',  class_num='08051903').insert()
# Student.where(name='Jack', class_num='2019213056').delete()

# Student.where(name='Jack', class_num='2019213056').update(stu_num='2019213056', class_num='08051903')


# what's next
# fetchall tuple -> dict


s = Student.where(name='Jack').need('class_num', 'stu_num').select()
print(s)

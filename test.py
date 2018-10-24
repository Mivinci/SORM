from dev.sorm import Model, StrField, IntField, TimeField


class User(Model):
    name = StrField(maxlen=25)
    age = IntField(default=23)
    first_time = TimeField(auto_update=True)


class Student(Model):
    __table__ = 'student_info'
    name = StrField()
    stu_num = StrField()
    class_num = StrField()
    first_time = TimeField()


Student.migrate().create()

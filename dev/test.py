from sorm import Model, Database, StrField, IntField, DatetimeField

db_config = {
    'user': 'root',
    'password': 'qwerty',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'jwzx',
    'charset': 'utf8'
}
Database.connect(**db_config)


class User(Model):
    name = StrField(maxlen=25, default=None)
    age = IntField(maxlen=11, default=None)
    first_time = DatetimeField()


# User.where(id=1, name='Tom').select()
User.migrate().create()


class Student(Model):
    __table__ = 'student_'
    name = StrField(maxlen=25, default=None)
    stu_num = StrField(maxlen=25, default=None)
    class_num = StrField(maxlen=25, default=None)
    first_num = DatetimeField()


Student.migrate().create()

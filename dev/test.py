from sorm import Model, Database, StrField, IntField, TimeField

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
    name = StrField(maxlen=25)
    age = IntField(default=23)
    first_time = TimeField(auto_update=True)


# User.where(id=1, name='Tom').select()
User.migrate().create()


class Student(Model):
    __table__ = 'student_info'
    name = StrField()
    stu_num = StrField()
    class_num = StrField()
    first_time = TimeField()


Student.migrate().create()


from sorm import Model, Database, StrField, IntField

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


# User.where(id=1, name='Tom').select()
User.migrate().create()


# sql = """select * from `stu` where `student_num` = %s"""
# res = Database.execute(sql, '2017213056')
# print(res)


from sorm import Database


db_config = {
    'user': 'root',
    'passwd': 'qwerty',
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'jwzx',
    'charset': 'utf8'
}


db = Database.connect(**db_config)
print(db.execute('select * from `stu` where WHERE `student_num` = 2017213068').fetchall())

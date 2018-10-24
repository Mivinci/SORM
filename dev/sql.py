import pymysql

table = 'student_info'
fields = [('name', {'type': 'VARCHAR', 'maxlen': '255', 'default': None}),
          ('stu_num', {'type': 'VARCHAR', 'maxlen': '255', 'default': None}),
          ('class_num', {'type': 'VARCHAR', 'maxlen': '255', 'default': None}), ('first_time', {'type': 'TIMESTAMP', 'default': 'NOW()', 'auto_update': False})]


# sql = f"""CREATE TABLE `{table}` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT, """
# for field in fields:
# 	sql += f"""`{field[0]}` {field[1]['type']}"""
# 	sql += f"""({field[1]['maxlen']}) """ if 'maxlen' in field[1].keys() else f""" """
# 	sql += f"""DEFAULT NULL, """ if not field[1]['default'] else field[1]['default']

# sql += f""") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""


# print(sql)

# what is the next
## pymysql execute test
# Something you gotta know
## indent error 


class Sql():
    sql = None

    @classmethod
    def create(cls, tb, fds):
        cls.sql = cls.get_create_sql(tb, fds)
        return cls

    @classmethod
    def insert(cls, tb, map):
        # cls.sql = cls.get_insert_sql(tb, map)
        return cls

    @classmethod
    def delete(cls):
        pass

    @classmethod
    def update(cls):
        pass

    @classmethod
    def select(cls):
        pass

    @classmethod
    def get_create_sql(cls, tb, fds):
        _sql = f"""CREATE TABLE `{tb}` (`id` int(11) unsigned NOT NULL AUTO_INCREMENT, """
        for field in fds:
            _sql += f"""`{field[0]}` {field[1]['type']}"""
            _sql += f"""({field[1]['maxlen']}) """ if 'maxlen' in field[1].keys() else f""" """
            _sql += f"""DEFAULT NULL""" if not field[1]['default'] \
                else f"""NOT NULL DEFAULT {field[1]['default']}"""
            _sql += f""" ON UPDATE CURRENT_TIMESTAMP, """ if 'auto_update' in field[1].keys() and field[1]['auto_update'] \
                else f""", """

        _sql += f"""PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
        return _sql


print(Sql.create(table, fields).sql)
# print(Sql.get_create_sql(table, fields))


conn = pymysql.connect(user='root', passwd='qwerty',
                       host='127.0.0.1', port=3306,
                       db='wx', charset='utf8')
with conn.cursor() as cursor:
    sql = Sql.create(table, fields).sql
    cursor.execute(sql)

conn.close()

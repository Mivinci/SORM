class Sql:
    sql = None

    @classmethod
    def create(cls, tb, fds):
        cls.sql = cls.get_create_sql(tb, fds)
        return cls

    @classmethod
    def drop(cls, tb):
        cls.sql = f"""DROP TABLE `{tb}`;"""
        return cls

    @classmethod
    def insert(cls, tb, data):
        cls.sql = cls.get_insert_sql(tb, data)
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

    @classmethod
    def get_insert_sql(cls, tb, data):
        _sql = f"""INSERT INTO `{tb}` ("""
        for key in data.keys():
            _sql += f"""{key}, """
        _sql += f""") VALUES ("""
        for val in data.values():
            _sql += f"""'{val}', """
        _sql += f""");"""
        return _sql


print(Sql.get_insert_sql('user', {'a': 'aaa', 'b': 'bbb', 'c': 1234}))

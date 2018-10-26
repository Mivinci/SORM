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
    def delete(cls, tb, data):
        cls.sql = cls.get_delete_sql(tb, data)
        return cls

    @classmethod
    def update(cls, tb, wheres, new):
        cls.sql = cls.get_update_sql(tb, wheres, new)
        return cls

    @classmethod
    def select(cls, tb, needs, params, fuzzy):
        cls.sql = cls.get_select_sql(tb, needs, params, fuzzy)
        return cls

    @classmethod
    def count(cls, tb, field):
        cls.sql = cls.get_count_sql(tb, field)
        return cls

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
        _sql = f"""INSERT INTO `{tb}` ({', '.join(data.keys())}) VALUES ('{"', '".join(data.values())}');"""
        return _sql

    @classmethod
    def get_select_sql(cls, tb, needs, params, fuzzy):
        _sql = f"""SELECT * """ if not needs or '*' in needs else f"""SELECT `{"`, `".join(needs)}` """
        _sql += f"""FROM {tb} WHERE """
        _sql += " AND ".join([f"""`{key}` = '{val}'""" for key, val in params.items()]) if not fuzzy \
            else " AND ".join([f"""`{key}` LIKE '%%{val}%%'""" for key, val in params.items()])
        _sql += f""";"""
        return _sql

    @classmethod
    def get_delete_sql(cls, tb, data):
        _sql = f"""DELETE FROM `{tb}` WHERE """
        _sql += " AND ".join([f"""`{key}` = '{val}'""" for key, val in data.items()]) + f""";"""
        return _sql

    @classmethod
    def get_update_sql(cls, tb, wheres: dict, new: dict):
        _sql = f"""UPDATE `{tb}` SET """
        _sql += ", ".join([f"""`{key}` = '{val}'""" for key, val in new.items()]) + f""" WHERE """
        _sql += " AND ".join([f"""`{key}` = '{val}'""" for key, val in wheres.items()]) + f""";"""
        return _sql

    @classmethod
    def get_count_sql(cls, tb, field):
        return f"""SELECT COUNT(`{field}`) FROM `{tb}`;"""

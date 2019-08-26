iNAME: int = 0
iDESC: int = 1

TYPE_STR:   str = "VARCHAR"
TYPE_INT:   str = "INT"
TYPE_TIME:  str = "TIMESTAMP"
TYPE_BOOL:  str = "INT"
TYPE_FLOAT32: str = "float"
TYPE_FLOAT64: str = "double"

DESC_KEY_TYPE:        str = "type"
DESC_KEY_CAPACITY:    str = "capacity"
DESC_KEY_SIZE:        str = "size"
DESC_KEY_DEFAULT:     str = "default"
DESC_KEY_NOTNULL:     str = "not_null"
DESC_KEY_AUTO_UPDATE: str = "auto_update"


class Convert:

    @classmethod
    def str(cls, field) -> str:
        return f"`{field[iNAME]}`" \
               f" {field[iDESC][DESC_KEY_TYPE]}({field[iDESC][DESC_KEY_CAPACITY]})" \
               f" {'NOT NULL' if field[iDESC][DESC_KEY_NOTNULL] else ''}" \
               f" DEFAULT {field[iDESC][DESC_KEY_DEFAULT] or 'NULL'}"

    @classmethod
    def int(cls, field) -> str:
        return f"`{field[iNAME]}`" \
               f" {field[iDESC][DESC_KEY_TYPE]}({field[iDESC][DESC_KEY_SIZE]})" \
               f" {'NOT NULL' if field[iDESC][DESC_KEY_NOTNULL] else ''}" \
               f" DEFAULT {field[iDESC][DESC_KEY_DEFAULT] or 0}"

    @classmethod
    def time(cls, field) -> str:
        return f"`{field[iNAME]}`" \
               f" {field[iDESC][DESC_KEY_TYPE]}" \
               f" {'NOT NULL' if field[iDESC][DESC_KEY_NOTNULL] else ''}" \
               f" DEFAULT {field[iDESC][DESC_KEY_DEFAULT] or 'NOW()'}" \
               f" {'ON UPDATE CURRENT_TIMESTAMP' if field[iDESC][DESC_KEY_AUTO_UPDATE] else ''}"

    @classmethod
    def bool(cls, field) -> str:
        return cls.int(field)

    @classmethod
    def float(cls, field) -> str:
        return f"`{field[iNAME]}`" \
               f" {field[iDESC][DESC_KEY_TYPE]}" \
               f" {'NOT NULL' if field[iDESC][DESC_KEY_NOTNULL] else ''}" \
               f" DEFAULT {field[iDESC][DESC_KEY_DEFAULT] or 0}"

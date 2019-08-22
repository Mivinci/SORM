from mporm import DSN


class ORM:
    dsn: DSN

    @classmethod
    def load(cls, dsn: DSN):
        cls.dsn = dsn

    @classmethod
    def load_file(cls, filename: str):
        pass
import unittest

from mporm.dsn import DSN
from mporm.sql import SingleSQL, SQL


class MyTestCase(unittest.TestCase):
    def test_SingleSQL_open(self):
        dsn = DSN(user="root", password="XJJ@none")
        conn1 = SingleSQL.open(dsn)
        conn2 = SingleSQL.open(dsn)
        SingleSQL.close()
        self.assertEqual(conn1 == conn2, True)

    def test_SQL_new(self):
        dsn = DSN(user="root", password="XJJ@none")
        conn1 = SQL(dsn).open()
        conn2 = SQL(dsn).open()
        conn1.close()
        conn2.close()
        self.assertEqual(conn1 == conn2, False)

    def test_SQL_execute(self):
        dsn = DSN(user="root", password="XJJ@none")
        with SQL(dsn).open().cursor() as cursor:
            cursor.execute("show tables")
        self.assertEqual(not cursor.fetchall(), False)


if __name__ == '__main__':
    unittest.main()

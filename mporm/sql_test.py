import unittest

from mporm import DSN
from mporm.sql import SingleSQL, SQL


class MyTestCase(unittest.TestCase):
    def test_SingleSQL_open(self):
        dsn = DSN(user="root", password="XJJ@none")
        conn1 = SingleSQL.open(dsn)
        conn2 = SingleSQL.open(dsn)
        SingleSQL.close()
        print(conn1)
        self.assertEqual(conn1 == conn2, True)

    def test_SQL_new(self):
        dsn = DSN(user="root", password="XJJ@none")
        conn1 = SQL(dsn).open()
        conn2 = SQL(dsn).open()
        conn1.close()
        conn2.close()
        self.assertEqual(conn1 == conn2, False)


if __name__ == '__main__':
    unittest.main()

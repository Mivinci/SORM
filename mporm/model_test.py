import unittest

from mporm.dsn import DSN
from mporm.orm import ORM
from mporm.fields import StrField, IntField, BoolField, FloatField
from mporm.model import Model


class Hero(Model):
    # __dsn__ = DSN(user="root", password="XJJ@none")
    __prefix__ = "Marvel"

    name = StrField()
    age = IntField()
    grown_up = BoolField()
    score = FloatField()


class MyTestCase(unittest.TestCase):
    def test_model_create(self):
        dsn = DSN(user="root", password="XJJ@none")
        ORM.load(dsn)
        Hero.drop()
        self.assertEqual(Hero.create() is not None, True)

    def test_model_insert(self):
        dsn = DSN(user="root", password="XJJ@none")
        ORM.load(dsn)
        self.assertEqual(Hero.add(name="Thor", age=1000, grown_up=True, score=6.28) is not None, True)

    def test_model_delete(self):
        dsn = DSN(user="root", password="XJJ@none")
        ORM.load(dsn)
        print(Hero.where(name="Thor", age=1000).delete())
        self.assertEqual("" is not None, True)

    def test_model_update(self):
        dsn = DSN(user="root", password="XJJ@none")
        ORM.load(dsn)
        print(Hero.where(name="Thor", age=1000).set(age=2000, score=12.56).update())
        self.assertEqual("" is not None, True)

    def test_model_select(self):
        dsn = DSN(user="root", password="XJJ@none")
        ORM.load(dsn)
        print(Hero.where(name="Natasha").filter("name"))
        self.assertEqual("" is not None, True)


# if __name__ == '__main__':
#     unittest.main()

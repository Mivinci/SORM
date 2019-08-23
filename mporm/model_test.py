import unittest

from mporm.dsn import DSN
from mporm.sql import ORM
from mporm.fields import StrField, IntField, BoolField, FloatField, Field
from mporm.model import Model


class Hero(Model):
    __prefix__ = "Marvel"

    name = StrField()
    age = IntField()
    grown_up = BoolField()
    score = FloatField()


class MyTestCase(unittest.TestCase):
    def test_model_create(self):
        ORM.load_file("db.toml")
        Hero.drop()
        self.assertEqual(Hero.create() is not None, True)

    def test_model_insert(self):
        ORM.load_file("db.toml")
        self.assertEqual(Hero.add(name="Thor", age=1000, grown_up=True, score=6.28) is not None, True)

    def test_model_delete(self):
        ORM.load_file("db.toml")
        print(Hero.where(name="Thor", age=1000).delete())
        self.assertEqual("" is not None, True)

    def test_model_update(self):
        ORM.load_file("db.toml")
        print(Hero.where(name="Thor").set(name="Peter Parker", age=18).update())
        self.assertEqual("" is not None, True)

    def test_model_find(self):
        ORM.load_file("db.toml")
        print(Hero.where(name="Natasha").find())
        # print(Hero.take(2))
        self.assertEqual("" is not None, True)


# if __name__ == '__main__':
#     unittest.main()


# @test
def test_model_declare():

    print("id", Hero.id.__dict__)
    print("created_at", Hero.created_at.__dict__)
    print("updated_at", Hero.updated_at.__dict__)

    for key, value in Hero.__dict__.items():
        if isinstance(value, Field):
            print(key, value.__dict__)
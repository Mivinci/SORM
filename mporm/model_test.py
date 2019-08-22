from mporm.dsn import DSN
from mporm.fields import StrField, IntField, BoolField, FloatField, Field
from mporm.model import Model
# from freetest import test, T
from mporm.orm import ORM


class Hero(Model):
    # __dsn__ = DSN(user="root", password="XJJ")
    __prefix__ = "Marvel"

    name = StrField()
    age = IntField()
    grown_up = BoolField()
    score = FloatField()


# @test
def test_model_declare():

    print("id", Hero.id.__dict__)
    print("created_at", Hero.created_at.__dict__)
    print("updated_at", Hero.updated_at.__dict__)

    for key, value in Hero.__dict__.items():
        if isinstance(value, Field):
            print(key, value.__dict__)


# @test
def test_model_new():
    dsn = DSN(user="root", password="XJJ@none")
    ORM.load(dsn)
    # Hero.where(name="Thor").filter("name", "age")
    Hero.create()


if __name__ == '__main__':
    # test_all()
    # test_model_declare()
    test_model_new()


from mporm.fields import StrField, IntField, BoolField, FloatField, Field
from mporm.model import Model
# from freetest import test, T


class Hero(Model):
    __prefix__ = "Marvel"
    name = StrField(not_null=True)
    age = IntField()
    grown_up = BoolField(False)
    score = FloatField()


# @test
def test_model_declare():

    print("created_at", Hero.created_at.__dict__)
    print("updated_at", Hero.updated_at.__dict__)

    for key, value in Hero.__dict__.items():
        if isinstance(value, Field):
            print(key, value.__dict__)


# test
def test_model_new():
    Hero.where(name="Thor").filter("name", "age")


if __name__ == '__main__':
    # test_all()
    test_model_new()


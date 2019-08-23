from mporm import ORM, DSN, Model, StrField, IntField, BoolField, FloatField


ORM.load_file("db.toml")


class Hero(Model):
    __prefix__ = "Marvel"

    name = StrField()
    age = IntField()
    grown_up = BoolField()
    score = FloatField()


print(Hero.take())
print(Hero.where(name="Thor").findone())

ORM.close()
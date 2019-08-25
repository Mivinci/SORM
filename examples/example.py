from mporm import ORM, Model, StrField, IntField, BoolField

ORM.load_file("db.toml")


class Hero(Model):
    __prefix__ = "Marvel"
    age = IntField()
    name = StrField()
    alive = BoolField(default=True)


Hero.create()

# CRUD
Hero.add(name="Thor", age=1000)
Hero.where(name="Thor").set(age=1001).update()
Hero.where(alive=True).order("created_at", desc=True).limit(10).offset(0).find()
Hero.where(name="Thor", age=1001).delete()

Hero.drop()

ORM.close()

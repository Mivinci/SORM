```
 _ __ ___  _____  ___  _ __  _ __ ___
| '_ ` _ \|  __ \/ _ \| `__/| '_ ` _ \
| | | | | | |___| |_| | |   | | | | | |
|_| |_| |_|_|    \___/|_|   |_| |_| |_|
```

**mporm** is an ORM tool for MySQL written in Python. [简体中文](https://github.com/Mivinci/mporm/blob/master/README_zh.md)

<br/>

## Get Started

### Install

```bash
pip3 install mporm
```

### Overview

#### Features

- gorm-like API
- Automatically set `uuid` as default id
- Automatically set `created_at` and `updated_at`

#### Quick Start

```python
from mporm import ORM, DSN, Model, StrField, IntField

ORM.load(DSN(user="xxxx", password="xxxx"))


class Hero(Model):
    __prefix__ = "Marvel"
    name = StrField()
    age = IntField()

Hero.create()

# CRUD
Hero.add(name="Thor", age=1000)
Hero.where(name="Thor").set(age=1001).update()
Hero.where(name="Thor").find()
Hero.where(name="Thor").delete()

Hero.drop()
```

#### Connect to Database

**mporm** can only  connect MySQL database, and have two different ways to load configs of database

##### Load By DSN

The minimum code that loads by dsn is wriiten as

```python
from mporm import ORM, DSN

ORM.load(DSN(user="xxxx", password="xxxx"))
```

Because mporm will automatically set other configs as `host` = "localhost", `port` = 3306, `database` = "test", `charset` = "utf8"

Of course you can fill all the configs by yourself

##### Load From Toml File

You can write all the configs in a toml file like

```toml
[database]
user = "xxxx"
password = "xxxx"
host = "xxxx"
port = 3306
database = "xxxx"
charset = "xxxx"
```

Then use `load_file` method

```python
from mporm import ORM

ORM.load_file("path/to/toml")
```

**Note** that if you use the second way, remember **all the 6** configs needs to be written in the toml file.

<br/>

## CRUD Interfaces

### Insert

### Update

### Select

### Delete
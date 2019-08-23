```
 _ __ ___  _____  ___  _ __  _ __ ___
| '_ ` _ \|  __ \/ _ \| `__/| '_ ` _ \
| | | | | | |___| |_| | |   | | | | | |
|_| |_| |_|_|    \___/|_|   |_| |_| |_|
```

![](https://img.shields.io/badge/Python-3%2B-yellowgreen) ![](https://img.shields.io/badge/MySQL-5.5%2B-yellowgreen) ![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-blue)

**mporm** is an ORM tool written in Python with only the fundamental CRUD API for MySQL(5.5+) [简体中文](https://github.com/Mivinci/mporm/blob/master/README_zh.md)

<br/>

## Overview

### Features

- [x] gorm-like API
- [x] Automatically use `uuid` as field `id`
- [x] Automatically set `created_at` and `updated_at`

### Install

```bash
pip3 install mporm
```

### Quick Start

```python
from mporm import ORM, DSN, Model, StrField, IntField

ORM.load(DSN(user="xxxx", password="xxxx"))


class Hero(Model):
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

### Connect to Database

**mporm** can only  connect MySQL database, and has two different ways to load configs of database

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

### Table Prefix

You can define a model with an attribute `__prefix__` , for example:

```python
from mporm import Model

class Hero(Model):
  __prefix__ = "Marvel"
  ...
  
Hero.create()  
```

This will create a new table named "marvel_hero"

<br/>

## CRUD Interfaces

We have defined a model like

```python
class Hero(Model):
    __prefix__ = "Marvel"
    name = StrField()
    age = IntField()
```

### Insert

There are two methods you can choose from:

```python
Hero.new(name="Thor", age=1000).insert()
```

or simply use

```python
Hero.add(name="Thor", age=1000)
```

The SQL statement that'll be executed is

```sql
insert into `marvel_hero` (name, age) values ('Thor', 1000);
```

### Select

#### Query

```python
Hero.first()
## select * from `marvel_hero` order by created_at limit 1;

Hero.last()
## select * from `marvel_hero` order by created_at desc limit 1;

Hero.take()
## select * from `marvel_hero` limit 1;
```

Plus they can take an argument

```python
Hero.first(10)
## select * from `marvel_hero` order by created_at limit 10;

Hero.last(10)
## select * from `marvel_hero` order by created_at desc limit 10;

Hero.take(10)
## select * from `marvel_hero` limit 10;
```

#### Where

```python
Hero.where(name="Thor", age=1000).find()
## select * from `marvel_hero` where name = 'Thor' and age = 1000;

Hero.where(name="Thor", age=1000).findone()
## select * from `marvel_hero` where name = 'Thor' and age = 1000 limit 1;
```

Of course, Specified Fields Selecting is available

```python
Hero.where(name="Thor", age=1000).select("name").find()
## select name from `marvel_hero` where name = 'Thor' and age = 1000;
```

Or you can simply use

```python
Hero.where(name="Thor", age=1000).filter("name")
## select name from `marvel_hero` where name = 'Thor' and age = 1000;
```

#### Count

```python
Hero.where(name="Thor").count()
## select count(id) from `marvel_hero` where name = 'Thor';
```

Also custom count field is available

```python
Hero.where(name="Thor").count("age")
## select count(age) from `marvel_hero` where name = 'Thor';
```

#### Advanced

##### Order

```python
Hero.where(name="Thor").order("age", desc=True).find()
## select * from `marvel_hero` where name = 'Thor' order by age desc;
```

##### Limit

```python
Hero.where(name="Thor").limit(10).find()
## select * from `marvel_hero` where name = 'Thor' limit 10;
```

##### Offset

```python
Hero.where(name="Thor").offset(10).find()
## select * from `marvel_hero` where name = 'Thor' offset 10;
```

Of course, you  can use them like chains

```python
Hero.where(name="Thor").order("age").limit(10).offset(10).select("name", "age").find()
## select name, age from `marvel_hero` where name = 'Thor' order by age asc limit 10 offset 10;
```

### Update

```python
Hero.where(name="Thor").set(age=1001).update()
## update `marvel_hero` set age=1001 where name = 'Thor';
```

### Delete

```python
Hero.where(name="Thor").delete()
## delete from `marvel_hero` where name = "Thor";
```

**Note** that the methods `insert()` `update()` `delete()` return the amount of rows that're affected and method `find()` returns a `list-typed` query result and not to mention, the method `findone()` returns a `dict-typed` query result.

## Todo

- [ ] where-like

- [ ] where-or
- [ ] Where-<>
- [ ] custom sql statement execution

## Contribute

You can do anything to help deliver a better MPORM.

## License

@ XJJ, 2019~datetime.now()

Released under the [MIT License](https://github.com/Mivinci/mporm/blob/master/LICENSE)
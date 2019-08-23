```
 _ __ ___  _____  ___  _ __  _ __ ___
| '_ ` _ \|  __ \/ _ \| `__/| '_ ` _ \
| | | | | | |___| |_| | |   | | | | | |
|_| |_| |_|_|    \___/|_|   |_| |_| |_|
```

![](https://img.shields.io/badge/Python-3%2B-yellowgreen) ![](https://img.shields.io/badge/MySQL-5.5%2B-yellowgreen) ![](https://img.shields.io/badge/build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-blue)

mporm** 是一个 Python写的 MySQL(5.5+) 的 ORM 工具, 只含有基本的增删改查 API

<br/>

## Overview

### 特点

- [x] 类似gorm API
- [x] 自动使用`uuid`作为默认`id`
- [x] 自动添加 `created_at` 和 `updated_at` 字段

### 安装

```bash
pip3 install mporm
```

### 快速开始

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

### 数据库连接

**mporm** 只能连接 MySQL, 有两种方法加载数据库配置

##### 使用DSN加载

最简单的使用如下

```python
from mporm import ORM, DSN

ORM.load(DSN(user="xxxx", password="xxxx"))
```

mporm 会自动设置剩下的配置参数为 `host` = "localhost", `port` = 3306, `database` = "test", `charset` = "utf8"

当然你也可以自己填写剩下的参数

##### 从 toml 文件中加载

先建一个含有所有配置参数的toml文件

```toml
[database]
user = "xxxx"
password = "xxxx"
host = "xxxx"
port = 3306
database = "xxxx"
charset = "xxxx"
```

使用 `load_file()` 方法

```python
from mporm import ORM

ORM.load_file("path/to/toml")
```

**注意** 如果使用第二种从文件中加载数据库配置参数的方法, 需要将6项参数写完

### 表名前缀

可以像这样为定义的模型添加`__prefix__`属性

```python
from mporm import Model

class Hero(Model):
  __prefix__ = "Marvel"
  ...
  
Hero.create()  
```

这样会创建数据表名为 "marvel_hero"

<br/>

## CRUD 接口

假设定义的模型为

```python
class Hero(Model):
    __prefix__ = "Marvel"
    name = StrField()
    age = IntField()
```

### 增

有两种方法可以新增一条数据

```python
Hero.new(name="Thor", age=1000).insert()
```

或简单地使用

```python
Hero.add(name="Thor", age=1000)
```

上面代码将会执行的 SQL 语句为

```sql
insert into `marvel_hero` (name, age) values ('Thor', 1000);
```

### 查

#### 简单查找

```python
# 查找表里第一条记录
Hero.first()
## select * from `marvel_hero` order by created_at limit 1;

# 查找表里最后一条记录
Hero.last()
## select * from `marvel_hero` order by created_at desc limit 1;

# 无排序要求, 查找表里一条记录
Hero.take()
## select * from `marvel_hero` limit 1;
```

也可以输入简单查找的个数

```python
# 查找表里前10条记录
Hero.first(10)
## select * from `marvel_hero` order by created_at limit 10;

# 查找表里后10条记录
Hero.last(10)
## select * from `marvel_hero` order by created_at desc limit 10;

# 无排序要求, 查找表里10条记录
Hero.take(10)
## select * from `marvel_hero` limit 10;
```

#### 条件查找

```python
Hero.where(name="Thor", age=1000).find()
## select * from `marvel_hero` where name = 'Thor' and age = 1000;

Hero.where(name="Thor", age=1000).findone()
## select * from `marvel_hero` where name = 'Thor' and age = 1000 limit 1;
```

当然可以只查找特定的字段

```python
Hero.where(name="Thor", age=1000).select("name").find()
## select name from `marvel_hero` where name = 'Thor' and age = 1000;
```

或简单地使用

```python
Hero.where(name="Thor", age=1000).filter("name")
## select name from `marvel_hero` where name = 'Thor' and age = 1000;
```

#### 查找个数

```python
Hero.where(name="Thor").count()
## select count(id) from `marvel_hero` where name = 'Thor';
```

也可以自定义统计的字段

```python
Hero.where(name="Thor").count("age")
## select count(age) from `marvel_hero` where name = 'Thor';
```

#### 高级查找

##### Order (排序规则)

```python
Hero.where(name="Thor").order("age", desc=True).find()
## select * from `marvel_hero` where name = 'Thor' order by age desc;
```

##### Limit (查找个数)

```python
Hero.where(name="Thor").limit(10).find()
## select * from `marvel_hero` where name = 'Thor' limit 10;
```

##### Offset (偏移个数)

```python
Hero.where(name="Thor").offset(10).find()
## select * from `marvel_hero` where name = 'Thor' offset 10;
```

Of course, you  can use them like chains

```python
Hero.where(name="Thor").order("age").limit(10).offset(10).select("name", "age").find()
## select name, age from `marvel_hero` where name = 'Thor' order by age asc limit 10 offset 10;
```

### 改

```python
Hero.where(name="Thor").set(age=1001).update()
## update `marvel_hero` set age=1001 where name = 'Thor';
```

### 删

```python
Hero.where(name="Thor").delete()
## delete from `marvel_hero` where name = "Thor";
```

**注意**  `insert()` `update()` 和 `delete()` 方法返回的是影响的记录条数,  `find()` 方法返回的是列表类型的查找结果,  `findone()` 方法返回的是字典类型的查找结果

## Todo

- [ ] where-like 模糊查找
- [ ] where-or   或条件查找
- [ ] Where-<>  大小比较条件查找
- [ ] 自定义 SQL 语句执行

## Contribute

You can do anything to help deliver a better MPORM.

## License

@ XJJ, 2019~datetime.now()

Released under the [MIT License](https://github.com/Mivinci/mporm/blob/master/LICENSE)
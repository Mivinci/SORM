# SORM

为 python-Flask 项目提供简单的对象关系映射API

## 'S' stands for simple, swift and stupid.



### 使用前

需要的 py 库

```
pip3 install pymysql
```

或

```
pip3 -r requirement.txt
```



### 创建模型

如需创建表名为 'user'，若有字段 'id', 'name', 'age', 'first_time'

```python
from dev.sorm import Model, StrField, IntField, TimeField

class User(Model):    # 继承该库的 Model 类
    name = StrField() # 默认值为NULL，默认最大长度255
    age = IntField()  # 默认值为NULL，默认最大长度11
    first_time = TimeField()  #默认值为第一次插入数据的时间，默认自动更新为False
```

- 会自动生成自增的主键 `id`
- 会自动以类名的小写来生成表名

也可以自定义初始值

```python
class User(Model):
    __table__ = 'user_info'  # 没这行 默认的表名为 'user'
    name = StrField(default='xxx', maxlen=25)
    age = IntField(default='xxx', maxlen=11)
    first_time = TimeField(default='2018-10-24 23:59:59', auto_update=True)
```

- 目前仅支持以上有的自定义初始值



### 创建表

```python
User.migrate().create()
```



### 删除表

```python
User.migrate().drop()
```



### 增加一条数据

若要增加的纪录为：Tom 23

```python
User.new(name='Tom', age=23).insert()
```



### 删除一条数据

若要删除name为Tom，age为 23 的记录

```python
User.where(name='Tom', age=23).delete()
```



### 更新一条记录

若要将 Tom 23 更新为 Jerry 23

```python
User.where(name='Tom', age=23).update(name='Jerry')
```



### 查询记录

若要查询 name为Tom， age为23的整条记录

```python
User.where(name='Tom', age=23).select()
```

- 返回的是字典列表  `[{}, {} ...]`  （你懂我的意思吧？）

若只需要查询某一字段值，如 `age`

```python
User.where(name='Tom', age=23).need('age').select()
```

其中若 `need()` 中输入的参数出现 `'*'` 也可以表示查询整条记录



### 总之

提供的使用接口有

```python
Object.migrate().create()                    # 建表
                .drop()                      # 删表
    			.count('字段名')              # 查询该字段记录值数量

Object.new(**kwargs).insert() 			     # 插入记录

Object.where(**kwargs).delete()              # 删除记录
                      .update(**kwargs)      # 更新记录
                      .select()              # 查询记录
                      .need(*args).select()  # 查询记录
                      
```



### 其他





下个版本预计添加:

​	· 外键 `ForeignKey(related='xxx')` 

ti go
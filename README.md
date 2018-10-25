# SORM

为 python-Flask 项目提供简单的对象关系映射APIs

## 'S' stands for simple, swift and stupid.



![huaji](images/huaji.GIF)



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

如需创建表名为 `user`，若有字段 `id`, `name`, `age`, `first_time`

```python
from dev.sorm import Model, StrField, IntField, TimeField

class User(Model):            # 继承该库的 Model 类
    name = StrField()         # 默认值为NULL，默认最大长度255
    age = IntField()          # 默认值为NULL，默认最大长度11
    first_time = TimeField()  #默认值为第一次插入数据的时间，默认自动更新为False
```

- 会自动生成自增的主键 `id`
- 会自动以类名的小写来生成表名

也可以自定义初始值

```python
class User(Model):
    __table__ = 'user_info'   # 没这行 默认的表名为 'user'
    name = StrField(default='xxx', maxlen=25)
    age = IntField(default='xxx', maxlen=11)
    first_time = TimeField(default='2018-10-24 23:59:59', auto_update=True)
```

- 目前仅支持以上有的自定义初始值



### 创建表

```python
User.migrate().create()
```

返回 0

若表已存在，就不需要调用这一个API啦





### 删除表

```python
User.migrate().drop()
```

返回 0



### 增加一条数据

若要增加的纪录为：Tom 23

```python
User.new(name='Tom', age=23).insert()
```

返回增加的记录的个数



### 删除一条数据

若要删除name为Tom，age为 23 的记录

```python
User.where(name='Tom', age=23).delete()
```

返回删除的记录的个数



### 更新一条记录

若要将 Tom 23 更新为 Jerry 23

```python
User.where(name='Tom', age=23).update(name='Jerry')
```

返回更新的记录的个数



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

该轮子还提供一些静态方法

`tuple_to_list() `  将存放字段名的元组与 pymysql 返回的查询记录的元组组装成字典列表，如

```python
from dev.sorm import tuple_to_list

keys = ('name', 'age')
data = (('Tom', 23), ('Jerry', 21))

res = tuple_to_list(keys, data)

print(res)
```

结果如下：

```python
[
    {
        'name', 'Tom',
        'age': 23
    },
    {
        'name': 'Jerry',
        'age': 21
    }
]
```

你懂我的意思吧 ~









<hr/>

#### 下个版本预计添加:

- 外键 `ForeignKey()`

  ```python
  # Something like:
  class Teacher(Model):
      ...
  
  class Student(Model):
      teacher = ForeignKey(related='id')
      ...
      
  Student.new(teacher=Teacher, ...).insert()
  ```



   

- 读取并执行自定义的sql语句

  ```python
  # Something like:
  Object.migrate().read('path/xxx.sql').do()   # 返回影响的行数
  ```




## Go get me some issues

![errors](images/errors.png)
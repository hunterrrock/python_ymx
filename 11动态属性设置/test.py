"""
# 魔法属性：__dict__
  可以获取这个类的所有属性：
  {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
    --》双下划线开头结尾的不管，以上代表这个类没有任何属性（非双下划线开头）
    {'__module__': '__main__', 'attr': 100, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
     --》上面看出这个类里有个attr属性
动态属性设置：
    涉及的四个内置函数：
    setattr()：动态设置属性
    getattr()：动态获取属性
    delattr()：动态删除属性
    hasatt()：判断属性是否存在

在代码执行的过程中给类添加属性
1：通过类名.属性名设置属性 (部分场景不适用）如下列的代码案例
MyClass.name = 'yan'
2:
setattr(类名，属性名，属性值）
setattr(对象，属性名，属性值）  --》给对象设置实例属性

动态获取属性：-->属性名不存在会报错（可以设置默认值，避免报错）
getattr(类名，属性名，默认值）  --》默认值可以省略
getattr(对象，属性名，默认值）

关键字：del
        用来删除数据的关键字，啥都能删(序列，只能删除可变，无法删除不可变序列中的数据，例如元组）

动态删除属性  ---》属性名不存在报错
delattr(类名，属性名）
判断属性是否存在：
1.
类名、对象名.属性名 加异常捕获去判断是否存在（存在不报错，不存在报错，再用异常捕获处理）
2、hasattr:存在返回True,不存在返回False
hasattr(类名，属性名）
hasattr(对象，属性名）
"""


class MyClass:
    attr = 100


key = 'name'
value = 'yan'
setattr(MyClass, key, value)
# -------------------------动态设置类属性案例---------------------------
# 这种场景很难用类名.属性的方法设置属性
data = {'name': 'yan', 'age': 10, 'gender': '男'}
for k, v in data.items():
    setattr(MyClass, k, v)

# 查出这个类所有的属性
print(MyClass.__dict__)

# -------------------------动态设置对象的属性---------------------------
m = MyClass()
data = {'name': 'yan', 'age': 10, 'gender': '男'}
for k, v in data.items():
    setattr(m, k, v)
# 查出这个对象的所有的属性
print(m.__dict__)
# 动态设置的属性，pycharm会标黄
print(m.name)
print(m.age)
print(m.gender)


# ------------------------动态获取属性-----------------------------
class MyClass2:
    attr = 100
    name = 'yan'
    age = 10


key = input("请输入要获取的属性")
key2 = 'attr'

# 这样无法获取：
# MyClass2.key2 或者 MyClass2.key 或 MyClass.'attr'

res1 = getattr(MyClass2, key2)
res2 = getattr(MyClass2, key, None)  # 如果属性名不存在就返回None

print(res1)
print(res2)

# --------------------del---------------------------
name = 'DSDFADSFASDF'
del name
# print(name)

li = [1, 2, 3, 4, 5]
del li[3]
print(li)

dic = {'a': 11, 'aa': 111}
del dic['aa']
print(dic)


class Mytest:
    age = 10
    name = 'yan'
    gender = '女'


del Mytest.age
print(Mytest.__dict__)

# -----------------动态删除属性----------------------------
# 以下场景如果使用del关键字则不适用（给的属性名是个字符串），可以选择用delattr来删除
key = input("请输入要删除的属性")
delattr(Mytest, key)
print(Mytest.__dict__)

# ------------------判断是否存在属性-------------------------
try:
    res = Mytest.name
except:
    print("没有该属性")
else:
    print("有该属性")

if hasattr(Mytest, 'name'):
    print("有该属性")

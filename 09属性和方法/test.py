"""
私有属性:仅供内部使用，不要在外部调用
    _单下划线开头：表示这是一个私有属性（没有真正的私有化，在外部依然可以调用）
    __双下划线开头：表示这是一个私有属性（类外部不可以调用）
私有方法
    _单下划线开头：表示这是一个私有方法（没有真正的私有化，类外部依然可以调用）
    __双下划线开头，表示这是一个私有方法（类外部不可以调用）

实例方法：
    只能通过对象调用（第一个参数self：代表对象本身）
    适用场景：方法内部如果要使用对象的属性或者方法，就要定义成实例方法
类方法：
    类方法的定义：
        先使用@classmethod 声明
    第一个参数cls:代表类本身，
    可以通过类直接去调用,也可以通过对象去调用
    适用场景：方法内部如果哟啊使用类属性或者类方法（不需要使用到对象的属性和方法），就可以定义成类方法
静态方法：
    静态方法的定义：
        先使用@staticmethod 声明
    适用场景：方法内部（既不需要使用类属性和类方法，也不需要用到对象属性和对象方法，就可以定义成静态方法

"""


# ------------------私有属性和私有方法--------------------------
class MyClass:
    _attr = 100
    __name = 'yan'

    def __get_info(self):
        print("------get_info")

    def func(self):
        print(self.__name)

    def _get_name(self):
        print("----getname-----")


b = MyClass()
print(b._attr)
# AttributeError: 'MyClass' object has no attribute '__name'：
# 在外部不能调用：
# print(b.__name)

b.func()
b._get_name()


# AttributeError: 'MyClass' object has no attribute '__get_info':
# b.__get_info()

# -----------------------静态方法--------------------------
class MyClass2:
    def func(self):
        print('_____func______实例方法')

    # 装饰器
    @classmethod
    def func_cls(cls):
        print('_____func______类方法')

    @staticmethod
    def func_static():
        print("_____func______静态方法")


MyClass2.func_cls()


class MyTest:
    attr = 100

    def __init__(self, name):
        self.name = name

    def func1(self):
        print(self.name)

    @classmethod
    def func2(cls):
        print(cls.attr)

    @staticmethod
    def func3():
        print("静态方法")

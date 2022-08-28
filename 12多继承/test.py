"""
多继承：一个类可以继承多个父类，同时继承多个父类
        如果同时继承的父类中有同名的方法，在调用这个方法时，会按照顺序去找，如下代码
        A和B都有func方法，m去调用的时候，会先从A去找这个方法，找不到再到B(如果自己有就用自己的）
"""


class BaseA:
    A = 100

    def func(self):
        print("---A---")


class BaseB:
    B = 200

    def func(self):
        print("---B---")


class Myclass(BaseA, BaseB):
    def func(self):
        print("---c----")
        super().func()


m = Myclass()
m.func()

"""
一个类可以继承多个父类
"""


class BaseA:
    A = 100

    def func(self):
        print("---A---")


class BaseB:
    B = 200

    def func(self):
        print("---B---")

class Myclass(B)

"""
定义类的两种形式：
class 类名：
    pass

class 类名(object):
    pass

object:python中所有类的顶级父类（基类）
继承：
    子类通过继承可以获得父类的属性和方法，提高开发小绿和代码的复用率
    私有属性无法继承

重写父类方法：
    重写：就是子类中有一个与父类同名的方法，在子类中的方法会覆盖掉父类中同名的方法
         如果想要子类重写并且依然保留父类这个同名方法的功能，就需要再调用重名的父类方法
         一般在你需要在这个父类方法上进行扩展时，才需要选择重写父类的方法
1：
父类名.方法名(self)       --》实例方法一定要加self
2：
super().方法名()
"""


# class Phone:
#     def call(self):
#         print("打电话的功能")
#
#
# class PhoneV2(Phone):
#     def send_msg(self):
#         print("发短信的功能")
#
#     def music(self):
#         print("放音乐")
#
#
# class PhoneV3(PhoneV2):
#     def pay(self):
#         print("手机支付")
#
#     def game(self):
#         print("玩游戏的功能")
#
# xiaomi = PhoneV3()
# xiaomi.call()
# xiaomi.music()
# xiaomi.send_msg()

# ------------------------继承的小案例------------------------
class BasePhone:
    attr = '移动电话'
    __attr2 = 10000

    def __init__(self, name):
        self.name = name

    def call(self):
        print(f"{self.name}打电话的功能")


class PhoneV2(BasePhone):
    # Phonev2虽然没有定义__init__方法，但是他继承了BasePhone类的__init__方法，所以在实例化的时候依然需要传入name参数
    def send_msg(self):
        print("发短信")

    def music(self):
        print("放音乐")


class Phonev3(BasePhone):
    def __init__(self, name, price):
        BasePhone.__init__(self, name)
        # 对该方法的功能扩展
        self.price = price


class Phonev4(BasePhone):
    def __init__(self, name, info):
        super().__init__(name)
        self.info = info


p = PhoneV2("诺基亚")
p2 = Phonev3("诺基亚", 6000)
p3 = Phonev4("诺基亚", "test")
p.call()
print(p.attr)
print(p2.price)
print(p3.info)
print(p3.name)

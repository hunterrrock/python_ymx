"""
核心的四个概念：
TestCase: 一个testcase的实例就是一个测试用例
TestSuite:  多个测试用例集合在一起。TestLoader:是用来加载TestCase到TestSuite中的
            当你有多个测试用例类，或者多个测试用例文件，想要一起执行就需要用到TestSuite（测试套件）.
            测试套件我们可以单独放到一个py文件里，运行该文件即可执行所有用例。
TestRunner: 用来执行测试用例的
fixture: 测试用例环境的搭建和销毁。测试前准备环境的搭建（setUp),执行测试代码（run)，以及测试后环境的还原（tearDown)



步骤：
一、用例编写
1、定义test开头的py文件
2、定义继承unittest.TestCase的用例类
3、定义test开头的测试用例方法

二、套件的使用
1、将测试用例加载到测试套件
  unitest.defaultTestLoader.discover(用例文件所在的路径）
三、测试运行程序
1、unittestreport里面的TestRunner
四、测试夹具fixture：
1、用例级别
2、测试类几倍
五、断言
"""
dict1 = {'username': 'python35', 'password': 'lemonban'}
def logprint(username,password):
    print(username)
    print(password)

logprint(**dict1)

# **dict -->拆包字典，{k1:v1,k2:v2}  ===>k1=v1,k2=v2
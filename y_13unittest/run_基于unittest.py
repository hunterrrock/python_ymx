"""
1.创建测试套件，加载测试用例到测试套件中
2.创建一个测试用例运行程序
3.执行测试用例

# 1.unittest中的TestSuite这个类，创建一个套件对象
suite = unittest.TestSuite()
# 2. 创建一个用例加载器
load = unittest.TestLoader()

# 3.使用用例加载器，将用例加载到测试套件中:(discover这个方法会根据你给的测试用例所在的路径中加载所有以Test开头的py文件，然后去找测试用例类(继承了unittest.TestCase的），再找Test开头的测试用例方法）
suite.addTest(load.discover(r'E:\PythonBase\y_13unittest'))
这三个步骤可以简写成一行
"""
import unittest
# unittest中的默认加载器调用discover方法，同样能够返回一个suite套件
suite = unittest.defaultTestLoader.discover(r'E:\PythonBase\y_13unittest')

# 创建一个测试用例运行程序
runner = unittest.TextTestRunner()

# 执行测试用例
runner.run(suite)
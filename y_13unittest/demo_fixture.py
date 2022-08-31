"""
fixture：测试夹具
用例级别：
setUp:每条测试用例执行之前都会执行： 用例级别的前置
        这个是----setUp-----
        这是第一条用例
        这个是----setUp-----
        这是第2条用例
        这个是----setUp-----
        这是第3条用例

tearDown:每条测试用例执行之后都会执行：用例级别的后置
        这个是----setUp-----
        这是第一条用例
        这个是-----tearDown-----
        这个是----setUp-----
        这是第2条用例
        这个是-----tearDown-----
        这个是----setUp-----
        这是第3条用例
        这个是-----tearDown-----
测试类级别：
setUpClass：测试类级别前置
    测试类中的用例执行前执行
tearDownClass：测试类级别后置
    测试类中所有的用例执行完毕之后执行
"""

import unittest


class TestYan(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("这个是----类方法setUpClass----")

    def setUp(self) -> None:
        print("这个是----setUp-----")

    def tearDown(self) -> None:
        print("这个是-----tearDown-----")

    def test_01(self):
        print("这是第一条用例")

    def test_02(self):
        print("这是第2条用例")

    def test_03(self):
        print("这是第3条用例")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这个是----类方法tearDownClass-------")

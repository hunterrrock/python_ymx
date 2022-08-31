"""
unittest提供的断言方法
assertEqual:断言两个数据是否相等 第一个为预期，第二个为实际
assertIn:成员断言 第一个数据是不是在第二个序列中
"""
import unittest


class TestAssert(unittest.TestCase):
    def test_01(self):
        print("这是第一条案例")
        # 这个方法是继承的unittest的TestCase类来的，这个类所提供的方法
        self.assertEqual(200,201)

    def test_02(self):
        print("这是第二条案例")
        data = ['11','22']
        n = '111'
        self.assertIn(n,data)


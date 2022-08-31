"""
unittest中测试用例的编写规范
1、定义一个测试用例类,要求：
    必须继承unittest模块中的TestCase类!!
2、在测试用例类，一个test开头的方法就是一条测试用例
3、将测试用例执行的代码逻辑写到对应的测试方法中
    第一步： 准备用例数据
    第二步： 调用被测的功能函数
    第三步： 断言
"""
from y_13unittest.login_func import login_check
import unittest

cases =[
    {'expected':{"code": 0, "msg": "登录成功"},
     'params':{'username': 'python35', 'password': 'lemonban'}
     }
]

class TestLogin(unittest.TestCase):

    def test_login_pass(self):
        # 每个用例下的文档注释会成为报告中的用例描述如下：
        """正常通过"""
        # 1.准备测试数据
        params = {'username': 'python35', 'password': 'lemonban'}
        expected = {"code": 0, "msg": "登录成功"}
        # 2.调用被测函数或接口
        res = login_check(**params)
        assert expected == res

    def test_login_uniserror(self):
        """用户名错误"""
        params = {'username': 'python34', 'password': 'lemonban'}
        expected = {"code": 1, "msg": "账号或密码不正确"}

        res = login_check(**params)
        assert expected == res

    def test_login_pwdiserror(self):
        """用户密码错误"""
        params = {'username': 'python35', 'password': 'lemonban1'}
        expected = {"code": 1, "msg": "账号或密码不正确"}

        res = login_check(**params)
        assert expected == res

    def test_login_unisnone(self):
        params = {'username': None, 'password': 'lemonban1'}
        expected = {"code": 1, "msg": "所有的参数不能为空"}

        res = login_check(**params)
        assert expected == res

if __name__ == '__main__':
    unittest.main()
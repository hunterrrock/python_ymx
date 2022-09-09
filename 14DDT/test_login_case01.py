"""

"""
import unittest
from login_func import login_check
from unittestreport import ddt, list_data

# cases列表中有多少个元素就会执行多少条用例
cases = [

    {'title': '登录成功', 'expected': {"code": 0, "msg": "登录成功"},
     'params': {'username': 'python35', 'password': 'lemonban'}
     },
    {'title': '账号不正确', 'expected': {"code": 1, "msg": "账号或密码不正确"},
     'params': {'username': 'python34', 'password': 'lemonban'}
     },
]


@ddt
class TestLogin01(unittest.TestCase):
    @list_data(cases)  # 存储用例数据
    def test_01_login(self, item):
        # 这里的item是我们定义来接受list_data中的cases中的每个元素
        data = item['params']
        expected = item['expected']
        res = login_check(**data)
        self.assertEqual(expected, res)

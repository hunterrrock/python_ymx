"""
TypeError: y_13unittest.login_func.login_check() argument after ** must be a mapping, not str
注意：excel读取出来的所有数据都是str类型，需要我们特殊处理，使用eval去掉双引号
"""

import unittest
from unittestreport import ddt, list_data
from login_func import login_check
from handle_excel import HandleExcel
from register_func import register


@ddt
class TestLogin001(unittest.TestCase):
    excel = HandleExcel(r'E:\PythonBase\y_17openpyxl&ddt\demo2.xlsx', 'Sheet1')
    cases= excel.read_excel()
    print(cases)

    @list_data(cases)
    def test_login(self, item):

        # 数据
        expected = eval(item['expected'])
        params = eval(item['params'])
        # 获取用例的行号,在此基础上+1
        row = item['case_id'] + 1

        # 调用login函数
        res = login_check(**params)
        # 第三步断言，并且把结果回写到excel中
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print("用例执行未通过")
            self.excel.write_excel(row=row, column=5, value="未通过")
            # 这里要将捕获的异常主动抛出，否则unittest未检测到断言异常就默认案例为通过（unittest以断言异常为检测案例是否通过的依据）
            raise e
        else:
            print("用例执行通过")
            self.excel.write_excel(row=row, column=5, value="通过")


@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(r'E:\PythonBase\y_17openpyxl&ddt\demo3.xlsx', 'Sheet1')
    cases = excel.read_excel()

    @list_data(cases)
    def test_regisetr(self, item):
        # 准备用例数据
        params = eval(item['params'])
        expected = eval(item['expected'])
        # 用例的行号
        row = item['case_id'] + 1
        # 调用函数
        # 用例数据为元组，拆包用一个*
        res = register(*params)
        # 断言
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            print("用例执行不通过")
            self.excel.write_excel(row=row, column=5, value='不通过')
            raise e
        else:
            print("用例执行通过")
            self.excel.write_excel(row=row, column=5, value='通过')

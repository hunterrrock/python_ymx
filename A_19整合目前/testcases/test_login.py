import unittest
from login_func import login_check
from unittestreport import ddt, list_data
from A_19整合目前.handle_excel import HandleExcel
from A_19整合目前.handle_log import mylog
"""
为了避免程序中创建多个日志收集器而导致日志重复记录，
那么我们可以只创建一个日志收集器，别的模块的使用时都导入这个日志收集器
"""
@ddt
class TestLogin(unittest.TestCase):
    excel = HandleExcel(r'E:\PythonBase\A_19整合目前\datas\login.xlsx', 'Sheet1')
    cases = excel.read_data()

    @list_data(cases)
    def test_login(self, item):
        # 准备测试数据
        params = eval(item['params'])
        expected = eval(item['expected'])
        row = item['case_id'] + 1
        # 调用被测函数
        res = login_check(**params)
        # 做断言并且输出日志
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            mylog.error('用例--【{}】执行不通过'.format(item['title']))
            self.excel.write_data(row=row, column=5, value='用例不通过')
            raise e
        else:
            mylog.info('用例--【{}】执行通过'.format(item['title']))
            self.excel.write_data(row=row, column=5, value='用例通过')

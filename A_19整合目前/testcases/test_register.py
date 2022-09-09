import logging
import unittest
from unittestreport import ddt, list_data
from A_19整合目前.handle_excel import HandleExcel
from register_func import register
from A_19整合目前.handle_log import mylog
"""
如果每个测试类中都创建了一个日志收集器，会导致日志重复输出
解决方法：创建日志收集器的代码不写在测试类中，可以写到handle_log的文件下，测试类中直接导入这个创建好的日志收集器即可
"""

@ddt
class TestRegister(unittest.TestCase):
    excel = HandleExcel(r'E:\PythonBase\A_19整合目前\datas\register.xlsx', 'Sheet1')
    cases = excel.read_data()


    @list_data(cases)
    def test_register(self, item):
        # 准备用例数据
        params = eval(item['params'])
        expected = eval(item['expected'])
        row = item['case_id'] + 1
        # 调用接口
        res = register(*params)
        # 断言：
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            mylog.error('用例--【{}】执行不通过'.format(item['title']))
            self.excel.write_data(row=row, column=5, value='不通过')
            # 打印详细的异常信息
            self.log.exception(e)
            raise e
        else:
            mylog.info('用例--【{}】执行通过'.format(item['title']))
            self.excel.write_data(row=row, column=5, value='通过')

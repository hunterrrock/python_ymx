import unittestreport
import unittest

suite = unittest.defaultTestLoader.discover(r'E:\PythonBase\y_17openpyxl&ddt')
runner = unittestreport.TestRunner(suite,tester='yan.ini',desc='yan测试报告',templates=2)
runner.run()
import unittestreport
import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'E:\PythonBase\y_13unittest\testcase')
runner = TestRunner(suite, tester='yan.ini', desc='yan测试生成的报告', templates=2)
runner.run()

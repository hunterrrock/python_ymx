import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'E:\PythonBase\14DDT')
runner =TestRunner(suite, tester='yan', desc='yan测试生成的报告', templates=2)
runner.run()

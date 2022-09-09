from unittestreport import TestRunner
import unittest

suit = unittest.defaultTestLoader.discover(r'E:\PythonBase\A_19整合目前\testcases')
runner = TestRunner(suit,tester='YAN',desc='YAN测试生成的报告',templates=2)
runner.run()
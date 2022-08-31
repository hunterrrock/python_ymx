"""
1、unitest用例执行顺序：
   同一个【用例类】中根据用例【方法名】按照ascii码来排序
   如果要主动去控制可以按照数字（ascii码中数字顺序）来
   例如：
   def test_01register
   def test_02password
   def test_03user_register

   同一个【用例文件】中的多个测试类是根据【类名】按照ASCII码排序
   同一个【文件夹】中的测试用例文件是根据【文件名】按照ASCII码排序
2、报告中的用例描述：就是测试方法的文档注释
"""
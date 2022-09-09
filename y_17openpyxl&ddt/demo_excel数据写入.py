"""


"""
import openpyxl

wb =openpyxl.load_workbook(r'E:\PythonBase\15openpyxl\demo1.xlsx')
sh = wb['Sheet1']

# excel中写入数据(文件必须在没有打开的状态下）
sh.cell(row=1,column=1,value='pythonn789')
# 写完后需要保存excel！！！
wb.save(r'E:\PythonBase\15openpyxl\demo1.xlsx')
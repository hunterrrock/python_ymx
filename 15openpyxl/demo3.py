import openpyxl

wb = openpyxl.load_workbook(r'E:\PythonBase\15openpyxl\demo1.xlsx')
sh = wb['Sheet1']
res = list(sh.rows)
# 获取excel中第一行的数据
title =[i.value for i in res[0]]
cases = []
# 遍历第一行以外的所有的行
for item in res[1:]:
    # 获取该行的数据
    data = [i.value for i in item]
    # 将第一行的数据和当前这行数据打包为字典
    dic = dict(zip(title,data))
    # 把字典添加到cases这个列表里
    cases.append(dic)
print(cases)
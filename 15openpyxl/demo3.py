import openpyxl

wb = openpyxl.load_workbook(r'E:\PythonBase\15openpyxl\demo1.xlsx')
sh = wb['Sheet1']
res = list(sh.rows)
print(res)
title = [i.value for i in res[0]]
print(title)
cases = []
for item in res[1:]:
    data = [i.value for i in item]
    dic = dict(zip(title,data))
    cases.append(dic)
print(cases)
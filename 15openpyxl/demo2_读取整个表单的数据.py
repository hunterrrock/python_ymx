import openpyxl

wb = openpyxl.load_workbook(r'E:\PythonBase\15openpyxl\demo1.xlsx')
sh = wb['Sheet1']

res = list(sh.rows)
print(res)
# title = res[0]
# n = []
# for i in title:
#     n.append(i.value)
# print(n)
# 获取excel中第一行数据
title = [i.value for i in res[0]]
# r1 = [i.value for i in res[1]]
# print(dict(zip(title, r1)))
# r2 = [i.value for i in res[2]]
# print(dict(zip(title, r2)))
cases = []
for item in res[1:]:
    data = [i.value for i in item]
    dic = dict(zip(title,data))
    cases.append(dic)
print(cases)

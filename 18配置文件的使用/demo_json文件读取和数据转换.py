"""
python中的字典---》对应的json中叫做对象
python中的列表----》对应的json中叫做数组
注意点：json数据中的字符串引号都要使用双引号

json.load：读取文件中的json数据并且自动转换为对应的py中相关的数据类型

python中的数据为空：None   -->json:null
python:True --->json:true
python:false --->json:false
json模块：
load:读取json文件转为对应的python数据
loads:将json字符串转为python数据
dumps:将python数据转换为json字符串
"""
import json

with open(r'E:\PythonBase\18配置文件的使用\datas', mode="r", encoding='utf-8') as f:
    res = json.load(f)
print(res)
print(res['logging'], type(res['logging']))



dic = {'aa': None, 'bb': 'python', 'cc': True, 'dd': False, 'ee': [11, 22, 33]}

# --------------python列表或字典转为json（json串：字符串）----------------------------
res = json.dumps(dic)
print(res)
print(type(res))  # --->转换为字符串类型

# ---------------json转python-------------------------------------------
json_str = '{"aa": null, "bb": "python", "cc": true, "dd": false, "ee": [11, 22, 33]}'
# 不能直接使用eval转为字典，因为null和true，false为json语法，python不认识
# print(eval(json_str))  -----》会报错
res = json.loads(json_str)
print(res)
print(type(res))
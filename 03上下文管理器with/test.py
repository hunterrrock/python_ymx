"""
使用with操作文件的好处：会启动文件的上下文管理器，不需要关闭文件，会自动关闭文件

with:上下文管理器协议的启动器
with open...as xx:去操作文件会自动关闭文件
"""
# 1、打开文件，返回文件的句柄
with open(file=r'E:\PythonProject\01文件的基本操作\0822b.txt', mode='r', encoding='utf-8') as f:
    res = f.read()
    print(res)

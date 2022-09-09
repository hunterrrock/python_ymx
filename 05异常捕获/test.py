""""
代码中常见异常：
Name Error:变量没定义
Syntax Error:invalid syntax 语法错误
KeyError :键不存在
ModuleNotFound Error:没找到模块
TypeError: 类型错误

我们主要需要处理的异常类型：Excepetion  常规错误的基类

异常捕获关键字： try  except else finally
语法：
try:
    有可能会出错的代码
    try中只要某一行代码报错，会立马进入到except中执行，不会再继续执行try里面的代码
    (try会去检测代码执行是否出错）
except 异常类型（常规：Exception) as e:
    # 用e变量把错误保存起来
    当try里面的代码执行出现错误时，会执行except中的代码
    可以在这里对异常进行处理
else:
    try中的代码执行没有错误，则会执行else中的代码
finally:
    不管try中的代码执行是否出错，始终都会执行finally中的代码
        (当try中的代码报错了，异常捕获时没有捕捉到或者异常处理的代码也报错了，那么后面的finally代码依然会执行，除了finally以外的代码都不会再被执行--》因为报错了）


except NameError as e:  # -->指定了nameerror类型的异常去捕获，其他异常类型捕获不到例如keyerror，如果报了keyerror的错误则会直接报错
"""
# -----------------------基础语法----------------------------
try:
    number = float(input("请输入一个数字："))
except:
    print("请输入数字！")

# ----------------------完整语法，捕获所有的常规异常类型和错误信息------------------------
try:
    number = float(input("请输入一个数字："))
except Exception as e:
    # 用e变量把错误保存起来
    print("您输入的不是数字！")
    print("错误信息：", e)

# ----------------------捕获指定的异常类型------------------------
dic = {'a': 11}

try:
    print(name)
    # print(dic['b'])
except NameError as e:
    print("错误:", e)

# ---------------------捕获多个异常类型：不同了异常类型不同的处理-----------------------
try:
    print("------1------------")
    print(name)
    print('------2------------')
    print(dic['b'])
except NameError as e:
    print("NameError的处理方案")
except KeyError as e:
    print("KeyError的处理方案")

# -------------------else的用法-------------------------------------
# 读取data.txt文件中的内容，再写入：python你好;
# 读取文件，如果文件存在则进行写入，不存在则捕获异常
try:
    with open('yaml语法.txt', 'r', encoding='utf-8') as f:
        res = f.read()
except Exception as e:
    print("该文件不存在")
    print("错误：", e)
else:
    with open('yaml语法.txt', 'w', encoding='utf-8') as f:
        f.write('hello,python')

# ----------------------------finally的用法-------------------------------
try:
    res = 11 + '11'
except NameError as e:
    print("代码出错了")
    print("错误：", e)
else:
    print("代码没出错")
finally:
    print("finally始终执行")
print("-----------99999---------------------")



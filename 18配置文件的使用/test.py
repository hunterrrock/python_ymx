"""
配置文件格式：ini，conf,cfg
为什么要做配置文件？
    将所有的代码和配置都变成模块化可配置化，提高代码的重用性，作为可配置化，就不用一直修改代码
    多处地方需要用同一个参数，这个时候最好是配置化
配置文件对象 配置项的等号后面不要加引号
    section:配置块  用[]括起来的
    option：配置项
python中操作配置文件：configparser
"""
"""from configparser import ConfigParser

# 第一步：创建一个配置文件解析器对象
cp = ConfigParser()
# 第二步：读取配置文件中的内容到配置文件解析器中
cp.read(r'E:\PythonBase\18配置文件的使用\yan', encoding='utf-8')
# 第三步：读取配置内容
# 方法一：get:使用get方法读取的配置内容都会被当成字符串
res = cp.get('logging', 'name')
# 方法二：getint:读取数值类型的数据，读出来是int类型
port = cp.getint('mysql', 'port')
# 方法三：getboolean：读取布尔类型数据
status = cp.getboolean('mysql', 'status')
# 方法四：getfloat:读取浮点类型数据
float1 = cp.getfloat('mysql', 'float')

print(res, type(res))
print(port, type(port))
print(status, type(status))
print(float1, type(float1))"""

# --------------------配置文件内容写入-----------------------------
"""cgp = ConfigParser()
cgp.read(r'E:\PythonBase\18配置文件的使用\yan', encoding='utf-8')

cgp.set('mysql', 'name', 'yanyan')
# cgp.write(fp = open(r'E:\PythonBase\18配置文件的使用\yan', 'w', encoding='utf-8'))
with open(r'E:\PythonBase\18配置文件的使用\yan', 'w', encoding='utf-8') as f:
    cgp.write(f)"""

# -----------------yaml文件读取----------------------------------
import yaml

# yaml文件中数据要么是字典，要么是列表
with open(r'E:\PythonBase\18配置文件的使用\data', mode='r', encoding='utf-8') as f:
    res = yaml.load(stream=f, Loader=yaml.Loader)
print(res)
print(type(res))
print(res[0]['data'])

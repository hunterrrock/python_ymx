from configparser import ConfigParser
import json


class Config(ConfigParser):
    """在创建对象时，直接加载配置文件中的内容"""

    def __init__(self, conf_file):
        super().__init__()
        self.read(conf_file, encoding='utf-8')


class Config_Json():
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        with open(self.filename, mode='r', encoding='utf-8') as f:
            res = json.load(f)
        return res


conf = Config(R'E:\PythonBase\A_19整合目前\config\confi')

if __name__ == '__main__':
    conf = Config(R'E:\PythonBase\A_19整合目前\config\confi')
    name = conf.get('logging', 'name')
    level = conf.get('logging', 'level')
    filename = conf.get('logging', 'filename')
    sh_level = conf.get('logging', 'sh_level')
    fh_level = conf.get('logging', 'fh_level')

    jsonc = Config_Json(r'E:\PythonBase\A_19整合目前\config\conf')
    res = jsonc.read_json()
    print(res)

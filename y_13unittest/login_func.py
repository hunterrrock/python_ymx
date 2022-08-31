

def login_check(username=None, password=None):
    """
    登录校验函数
    :param username: 用户名
    :param password: 密码
    :return: dict type
    """
    if username != None and password != None:
        if username == 'python35' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "所有的参数不能为空"}



if __name__ =='__main__':
    f =login_check(username='',password='lemonban')
    print(f)
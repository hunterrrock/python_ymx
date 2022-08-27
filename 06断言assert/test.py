"""
assert:断言
assert 预期结果 == 实际结果  -->这行代码如果断言失败了，会报错：AssertionError
AssertionError：这个错误类型用来表示用例通过还是不通过



"""
# ---------------基本语法-------------------------
# 预期结果：
expected = '注册成功'
# 实际结果：
res = '注册成功'

assert expected == res

# ---------------和异常处理结合使用-----------------
exp = '成功了'
res1 = '失败了'
try:
    assert exp == res
except AssertionError as e:
    print("断言失败，用例执行失败")
else:
    print("断言通过，用例执行通过")

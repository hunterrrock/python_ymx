"""
raise:主动抛出异常

raise AssertionError
raise NameError("xxx没定义")

isinstance(a,xx) --->判断a是否是XX类型的数据,-->返回True或者False
"""


# ---------------使用----------------------
# raise AssertionError
# raise NameError("xxx没定义")

# ----------------raise应用场景--------------
# 限定参数的额类型，不是对应的类型，主动抛出异常
def add(a, b):
    # 判断a是不是int类型,
    if not isinstance(a, int):
        raise ValueError("a只能是int类型")
    if not isinstance(b, int):
        raise ValueError("b只能是int类型")
    return a + b


add("a", 11)

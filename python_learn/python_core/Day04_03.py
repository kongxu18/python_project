"""
生成器表达式
"""

list01 = [3, 'a', 4, 5, 6, 1.3, True, 'ss', 'cv', 'sr', 3.4]


def fun01():
    for item in list01:
        if type(item) == int:
            yield item


re = fun01()
for item in re:
    print(item)

# 生成器表达式
# 此时没有计算更没有结果
re = (item for item in list01 if type(item) == int)
# 一次循环一次计算一次结果
for item in re:
    print(item)

"""
练习 1，获取列表中所有字符串
    生成器函数
    生成器表达式
    列表推导式
"""


def fun02():
    for item in list01:
        if type(item) == str:
            yield item


re = fun02()
for item in re:
    print(item)

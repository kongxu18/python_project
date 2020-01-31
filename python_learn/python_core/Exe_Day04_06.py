"""
函数式编程 练习
"""
list01 = [3, 22, 34, 4, 5, 6, 77, 2]


# 找所有偶数
def fun01():
    for item in list01:
        if item % 2 == 0:
            yield item


# 找大于10的数
def fun02():
    for item in list01:
        if item > 10:
            yield item


# 找10到50 的数
def fun03():
    for item in list01:
        if 50 > item > 10:
            yield item


def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 10


def condition03(item):
    return 10 < item < 50


def find(func):
    for item in list01:
        if func():
            yield item

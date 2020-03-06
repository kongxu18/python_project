"""
    函数式编程 练习
"""
from common.list_helper import *


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return str(self.name) + '-' + str(self.hp) + '-' + str(self.atk) + '-' + str(self.defense)


list01 = [
    Enemy('玄秘', 86, 123, 56),
    Enemy('成亏', 0, 100, 5),
    Enemy('妖艳', 120, 130, 60),
    Enemy('灭吧', 0, 1309, 690)
]

""" 练习2
    在list_helper 中添加通用的筛选方法
    1。获取所有敌人名称
    2。计算所有敌人攻击力
    3。计算所有敌人名称和血量
"""


def select01(func):
    # 数据太多了 不要列表存储
    # result = []
    for item in list01:
        # result.append((item.name, item.hp))
        # result.append(handle01(item))
        # result.append(func(item))
        yield func(item)
    # return result


def handle01(item):
    return item.name


def handle02(item):
    return item.atk


for item in ListHelper.select(list01, lambda item: (item.name, item.hp)):
    print(item)

"""
    练习3 
    在list_helper 中添加通用的获取最大值方法
    1，获取攻击力最大的
    2。获取防御力最大的
    3。获取血量最高的
"""


def get_max01():
    max_value = list01[0]
    for item in list01:
        if item.atk > max_value.atk:
            max_value = item
    return max_value


a = get_max01()
print(a.name)


def get_max01():
    max_value = list01[0]
    for item in list01:
        if item.defense > max_value.defense:
            max_value = item
    return max_value


b = get_max01()
print(b.name)


# 提取变化
def handle01(item):
    return item.atk


def handle02(item):
    return item.defense


# 提取不变的
def get_max(func):
    max_value = list01[0]
    for item in list01:
        if func(max_value) < func(item):
            max_value = item
    return max_value


c = get_max(handle01)
print(c.name)
# 最终结果
print(ListHelper.get_max(list01, lambda item: item.atk))

"""
    练习4
    在list_helper 中添加通用的 升序排列方法
    1。按照攻击力进行升序排序
    2。按照防御力进行升序排序
    3。按照血量进行升序排序
"""


def fun_sort():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r].atk > list01[c].atk:
                list01[r], list01[c] = list01[c], list01[r]


# 提取变换点
def handle01_04(item):
    return item.atk


def handle02_04(item):
    return item.hp


def order_by(func):
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if func(list01[r]) > func(list01[c]):
                list01[r], list01[c] = list01[c], list01[r]


# order_by(handle01_04)
# fun_sort()
# for item in list01:
#     print(item)

# 最终版本
ListHelper.order_by(list01,lambda item:item.atk)
for item in list01:
    print(item)
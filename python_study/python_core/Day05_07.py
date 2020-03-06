"""
    高阶函数
"""

from common.list_helper import *


# 内置的高阶函数
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
# 1。filter
# 需求所有hp=0
re = filter(lambda item: item.hp == 0, list01)
for item in ListHelper.find(list01, lambda item: item.hp == 0):
    print(item)
for item in re:
    print(item)

# 2.map 获取所有姓名
for item in ListHelper.select(list01, lambda item: item.name):
    print(item)

re = map(lambda item: item.name, list01)
for item in re:
    print(item)

# 3. max  获取血量最大
print(ListHelper.get_max(list01, lambda item: item.hp))
print(max(list01, key=lambda item: item.hp))

# 4.min
# 5.排序 sorted

"""
    1.获取元组中 列表长度最大的列表
    2.根据敌人列表，获取所有敌人的姓名与血量与攻击力
    3。在敌人列表中，获取攻击力大于100所有活人
    4。根据防御力，对敌人列表进行降序排序
"""
tuple01 = ([1, 3, 2], [2, 2], [3, 3, 3, 3])
re = ListHelper.get_max(tuple01, lambda item: len(item))
print(re)
max(tuple01, key=lambda item: len(item))

re = map(lambda item: (item.name, item.hp, item.atk), list01)
for item in re:
    print(item)

re = filter(lambda item: item.atk > 100 and item.hp > 0, list01)
for item in re:
    print(item)
# 参数中 （，*， ）只要放了一个星，后面的参数需要使用关键字传参
re =sorted(list01,key=lambda item:item.atk,reverse=True)
for item in re:
    print(item)
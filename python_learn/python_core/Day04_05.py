"""
    函数式编程

"""


def fun01():
    print('fun01')


# 将函数赋值给一个变量
re = fun01
# 通过变量调用函数
re()


def fun02():
    print('fun02')


# 将函数作为函数的参数传递
# 将一个函数代码注入到另外一个函数体中
def fun03(func):
    print('fun03')
    func()


fun03(fun01)
"""
    函数式编程的思想
"""


class SkillDate:
    def __init__(self, id, name, atk, duration):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    def __str__(self):
        return str(self.name)


list_skill = [
    SkillDate(101, 'a', 5, 10),
    SkillDate(102, 'b', 8, 1),
    SkillDate(103, 'c', 10, 5),
    SkillDate(104, 'd', 7, 2),
]
"""
封装  分而治之 每个需求拆分
    变则疏之 （变化点做成一个类）将每个变化条件单独定义在函数中
"""


# 获取攻击比例大于6的所有技能
def func01():
    for item in list_skill:
        if item.atk > 6:
            yield item


def func02():
    for item in list_skill:
        if 4 < item.duration < 11:
            yield item


# 封装
def condition01(item):
    return item.atk > 6


def condition02(item):
    return 4 < item.duration < 11


# 继承隔离变化
def find(func):
    """
    通用查找方法
    :param func: 查找条件，函数类型
    :return:
    """
    for item in list_skill:
        """
        多态 调用父 变量，执行子 具体函数
        不同于子类重写父类方法，执行逻辑不同
        """
        if func(item):
            yield item


from common.list_helper import *

generator = ListHelper().find(list_skill, condition01)
for item in generator:
    print(item, '---')

"""
    在listhelper中 定义查找满足条件的单个对象
"""
# 查找编号是101

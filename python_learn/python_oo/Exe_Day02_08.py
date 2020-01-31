"""
类成员
定义老婆类，创建对象

"""


class Wife:
    count = 0

    def __init__(self, age):
        self.age = age
        Wife.count += 1

    @classmethod
    def print_wife(cls):
        print('我有%d个老婆' % cls.count)

    def wife(self):
        print(Wife.count)
wife01 = Wife(12)
wife02 = Wife(12)
wife03 = Wife(12)

Wife.print_wife()
# 也可以通过对象地址访问类成员
print(wife01.count)
# 也可以用类调用实例方法
Wife.wife(wife01)
"""
其他的语法形式
"""


class Student:
    def __init__(self):
        self.fun01()

    def fun01(self):
        # 也是创建实例变量
        self.a = 10


s01 = Student()
# 这也是创建实例变量
s01.name = '无忌'
s01.age = 12


print(s01.age, s01.name, s01.a)


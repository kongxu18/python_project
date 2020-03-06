print('module01------')
# 定义当前模块成员可以被   from module01 import * 导入的
__all__ = ['fun01']


def fun01():
    print('fun01 module01')


class Module:
    @staticmethod
    def fun02():
        print('Module01 fun02')


class Test:
    def __init__(self):
        self.__list01 = []

    @property
    def list01(self):
        return self.__list01

    def append(self, val):
        self.list01.append(val)

    def dellist(self, val):
        for item in self.list01:
            if val == item:
                self.list01.remove(item)


a = Test()

a.append(1)
a.append(2)
a.append(3)
a.dellist(2)
print(a.list01)


def _fun02():
    print('moudle01 fun02')


class Myclass:
    @staticmethod
    def fun03():
        print('myclass fun03')

print(__name__)
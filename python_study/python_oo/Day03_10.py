"""
面向对象 封装设计思想
    老张开车去东北
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def go_to(self, str_postion, type):
        type.run(str_postion)


lz = Person('老张')


class Car:
    def run(self, position):
        print('行驶', position)


car = Car()
lz.go_to('东北', car)

"""
面向对象  小明在招商银行取钱
"""


class PersonBank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    # 这个取钱行为应该谁做
    def draw_money(self, person, value):
        self.money -= value
        person.money += value
        print(person.name, person.money)


xm = PersonBank('小明', 0)
zs = Bank('招商', 1000)
zs.draw_money(xm, 600)

print(zs.money)

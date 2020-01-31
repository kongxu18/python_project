"""
练习：敌人类（攻击力0--100）
    抛出异常
"""


def fun01(**kwargs):
    print(kwargs)


fun01(a=1)
fun01(a=1, b=2, c=3)


class AtkError(Exception):
    def __init__(self, value):
        super().__init__('错误了')
        self.value = value


class Enemy:
    def __init__(self, atk):
        self.attack = atk

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if value > 100:
            raise AtkError(value)
        else:
            self.__attack=value


Enemy(200)
try:
    Enemy(200)
except AtkError as e:
    print('错误了')
    print(e)
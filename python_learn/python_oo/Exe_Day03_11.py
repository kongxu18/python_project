"""
面向对象思想
张无忌教 赵敏 九阳神功
赵敏 教 张无忌 化妆
张无忌 上班 挣了 100
赵敏 上班 挣了 600
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

    def teach(self, other, skill):
        print(self.name, '教', other.name, skill)

    def work(self, money):
        print(self.name, '上班', money)


zwj = Person('张无忌')
zm = Person('张敏')
zwj.teach(zm, '神功')
zwj.work(1000)
"""
玩家（攻击力） 攻击 敌人（血量） ，敌人 受伤 掉血 可能死亡（掉装备，加分）
敌人 攻击 玩家 ，玩家受伤掉血，碎屏 可能死亡（游戏结束）
"""

""" 
类体会行为上的不同
"""


class Player:
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, other):
        print('玩家攻击敌人')
        # 通过敌人对象地址，调用实例方法
        other.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print('玩家受伤剩余血', self.hp)
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print('玩家死亡')


class Enemy:
    def __init__(self, atk, hp):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        # 受伤的逻辑
        self.hp -= value
        print('敌人受伤剩余', self.hp)
        if self.hp <= 0:
            self.__death()

    # 私有的死亡方法
    def __death(self):
        print('死亡', '掉装备', '加分')

    def attack(self, other):
        print('敌人攻击玩家')
        other.damage(self.atk)


e01 = Enemy(50, 100)
p01 = Player(60, 100)
p01.attack(e01)
p01.attack(e01)

e01.attack(p01)
e01.attack(p01)
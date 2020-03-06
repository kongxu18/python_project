"""
静态方法
"""


class Vector2:
    """
    二维向量，表示方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 函数表示方向
    @staticmethod
    def left():
        """DoubleListHelper
        静态方法 对数据的处理
        :return:
        """
        return Vector2(0, -1)

    @staticmethod
    def right():
        """
        表达右边
        :return:
        """
        return Vector2(0, 1)

    @staticmethod
    def up():
        """
        往上移动
        :return:
        """
        return Vector2(-1, 0)

    @staticmethod
    def down():
        """
        向下移动
        :return:
        """
        return Vector2(1, 0)


# 一个位置加上一个方向

list01 = [
    ['00', '01', '02', '03'],
    ['10', '11', '12', '13'],
    ['20', '21', '22', '23'],
]

pos01 = Vector2(1, 2)

# 类名掉用静态方法
l01 = Vector2.left()
pos01.x += l01.x
pos01.y += l01.y

print(pos01.x, pos01.y)
"""
    练习
"""


# 获取 '10' 右边三个元素
class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
        获取指定位置，指定方向的，指定数量的元素
        :return:
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result


re = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
print(re)

"""
练习
"""
# 获取 '13'位置 向左三个元素
re = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
print(re)

# 获取22位置，向上 2个元素
re = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
print(re)

"""
    定义敌人类
    数据
    行为
"""


class Enemy:
    enemy_list = []

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def print_info(self):
        print(self.name, self.hp, self.attack, self.defense)

    def append_enemy(self):
        Enemy.enemy_list.append(self)


enemy1 = Enemy('a', 100, 120, 58)
enemy1.append_enemy()
enemy2 = Enemy('b', 100, 20, 38)
enemy2.append_enemy()
enemy3 = Enemy('c', 10, 120, 5)
enemy3.append_enemy()


def find01():
    for item in Enemy.enemy_list:
        if item.name == 'd':
            return item


# 如果没找到返回值为None
e01 = find01()
if e01:
    e01.print_info()
else:
    print('aaaaaa')


# 查找所有死亡的人

# 查找平均攻击力
def calculate01():
    sum_atk = 0
    for item in Enemy.enemy_list:
        sum_atk += item.attack
    return sum_atk / len(Enemy.enemy_list)


print(calculate01())


# 删除攻击力小于5的
def delete01():
    # 倒着删除
    for i in range(len(Enemy.enemy_list) - 1, -1, -1):
        if Enemy.enemy_list[i].defense < 10:
            del Enemy.enemy_list[i]


delete01()
for item in Enemy.enemy_list:
    print(item.name)

# 所有人攻击力 加50

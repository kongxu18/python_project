"""
手雷炸了，可能伤害敌人 玩家 生命 还可能伤害未知事物
"""


class Victim:
    def get_harm(self):
        pass


class Grenades:
    def __init__(self):
        pass

    def harm(self, victim):
        victim.get_harm()


class Player(Victim):
    def get_harm(self):
        print('玩家受伤')


grenades = Grenades()
p01 = Player()
grenades.harm(p01)

"""
定义图形管理器类
    管理所有图形
    提供计算所有图形面积方法
"""


class GraphicManager:
    def __init__(self):
        self.__graphics = []

    def add_graphic(self, graphic):
        if isinstance(graphic, Graphic):
            self.__graphics.append(grenades)
        else:
            raise ValueError()

    def get_area(self):
        total = 0
        for item in self.__graphics:
            total += item.calculate_area()
        return total


class Graphic:
    def calculate_area(self):
        pass


class Rectanlge(Graphic):
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid

    def calculate_area(self):
        print('矩形', self.len * self.wid)

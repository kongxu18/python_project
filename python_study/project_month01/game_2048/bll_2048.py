"""
    游戏逻辑
"""

from model_2048 import *
import random


class GameCoreControl:
    def __init__(self):
        self.__list_merge = None
        self.__map = [[2, 0, 0, 2], [4, 4, 2, 2], [2, 4, 0, 4], [0, 0, 2, 2]]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾
        :param list_merge:
        :return:
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
        将数组 相同数字相加
        先将零移至末尾，再合并
        :param list_merger:
        :return:
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i], self.__list_merge[i + 1] = self.__list_merge[i] * 2, 0
                self.__zero_to_end()

    def __move_left(self):
        """
        向左移动
        :param list_source:
        :return:
        """
        for item in self.map:
            self.__list_merge = item
            self.__merge()

    def __move_right(self):
        for item in self.map:
            self.__list_merge = item[::-1]
            self.__merge()
            # 从右往左接受新列表 合并
            item[::-1] = self.__list_merge

    def __square_matrix_transpose(self):
        """
        方阵转置
        :param target_list:
        :return:
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = \
                    self.__map[c - 1][r], self.__map[r][c - 1]

    def __move_up(self):
        """
        向上移动，转置以后向左
        :return:
        """
        self.__square_matrix_transpose()
        self.__move_left()
        self.__square_matrix_transpose()

    def __move_down(self):
        """
        往下移动
        :param sqr_matrix:
        :return:
        """
        self.__square_matrix_transpose()
        self.__move_right()
        self.__square_matrix_transpose()

    def move(self, dir):
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        else:
            self.__move_right()

    def generate_new_number(self):
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2


    def __get_empty_location(self):
        """
        获取空位置
        :return:
        """
        self.__list_empty_location.clear()
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def is_game_over(self):
        # self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            pass


if __name__ == '__main__':
    controller = GameCoreControl()
    # controller.move_left()
    print(controller.map)
    # controller.move(DirectionModel.LEFT)
    controller.generate_new_number()
    print(controller.map)

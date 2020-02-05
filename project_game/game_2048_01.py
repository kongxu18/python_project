from abc import ABC

import pyglet

import pyglet
from pyglet.window import key
import random
import copy

WIN_WIDTH = 530
WIN_HEIGHT = 720
# 棋盘左下角坐标
STARTX = 15
STARTY = 110

# 每行的方块数目
WINDOW_BLOCK_NUM = 4
# 总宽度和每块的宽度
BOARD_WIDTH = (WIN_WIDTH - 2 * STARTX)
BLOCK_WIDTH = BOARD_WIDTH / WINDOW_BLOCK_NUM
# 方块的颜色
COLORS = {
    0: (204, 192, 179), 2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121),
    16: (245, 149, 99), 32: (246, 124, 95), 64: (246, 94, 59), 128: (237, 207, 114),
    256: (233, 170, 7), 512: (215, 159, 14), 1024: (222, 186, 30), 2048: (222, 212, 30),
    4096: (205, 222, 30), 8192: (179, 222, 30), 16384: (153, 222, 30), 32768: (106, 222, 30),
    65536: (69, 222, 30), 131072: (237, 207, 114), 262144: (237, 207, 114), 524288: (237, 207, 114),
    1: (204, 192, 179), 3: (204, 192, 179), 5: (204, 192, 179), 6: (204, 192, 179), 7: (204, 192, 179),
    9: (204, 192, 179), 10: (204, 192, 179), 11: (204, 192, 179), 12: (204, 192, 179), 13: (204, 192, 179),
    14: (204, 192, 179), 15: (204, 192, 179), 16: (204, 192, 179), 17: (204, 192, 179),
}
LABEL_COLOR = (110, 110, 101, 255)
BG_COLOR = (250, 248, 239, 255)
LINE_COLOR = (165, 165, 165, 225)

pyglet.font.load('STFangsong', 16)


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.game_init()

    def game_init(self):
        self.main_batch = pyglet.graphics.Batch()
        self.data = [[0 for i in range(WINDOW_BLOCK_NUM)] for j in range(WINDOW_BLOCK_NUM)]
        # 随机两个位置填充2或者4
        count = 0
        while count < 2:
            row = random.randint(0, WINDOW_BLOCK_NUM - 1)
            col = random.randint(0, WINDOW_BLOCK_NUM - 1)
            if self.data[row][col] != 0:
                count += 1
                continue
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            count += 1

        #         背景
        background_img = pyglet.image.SolidColorImagePattern(color=BG_COLOR)
        self.background = pyglet.sprite.Sprite(
            background_img.create_image(WIN_WIDTH, WIN_HEIGHT), 0, 0
        )

        #         title
        self.title_label = pyglet.text.Label(text='2048', bold=True,
                                             color=LABEL_COLOR, x=STARTX, y=BOARD_WIDTH + STARTY + 30 + 30,
                                             font_size=20, batch=self.main_batch
                                             )

        #         score
        self.score = 0
        self.score_label = pyglet.text.Label(text='Score = %d' % (self.score), bold=True,
                                             color=LABEL_COLOR, x=200, y=BOARD_WIDTH + STARTY + 30,
                                             font_size=36, batch=self.main_batch)

        #         help
        self.help_label = pyglet.text.Label(text='use up down left right to play', bold=True,
                                            color=LABEL_COLOR, x=STARTX, y=STARTY - 50,
                                            font_size=18, batch=self.main_batch)

    def draw_grid(self, startx, starty):
        rows = columns = WINDOW_BLOCK_NUM + 1
        #         水平线
        for i in range(rows):
            pyglet.graphics.draw(
                2, pyglet.gl.GL_LINES,
                ('v2f', (
                    startx, i * BLOCK_WIDTH + starty,
                    WINDOW_BLOCK_NUM * BLOCK_WIDTH + startx, i * BLOCK_WIDTH + starty
                )),
                ('c4B', LINE_COLOR * 2)

            )
        #             垂直线
        for j in range(columns):
            pyglet.graphics.draw(
                2, pyglet.gl.GL_LINES,
                ('v2f',
                 (
                     j * BLOCK_WIDTH + startx, starty,
                     j * BLOCK_WIDTH + startx, WINDOW_BLOCK_NUM * BLOCK_WIDTH + starty
                 )), ('c4B', LINE_COLOR * 2)
            )

    # 绘制方块
    def draw_tile(self, xywh, data):
        """
        绘制方块
        :param xywh: (x,y,方块宽，方块高)
        :param data: 方块内数字
        :return:
        """
        x, y, dx, dy = xywh
        color_rgb = COLORS[data] if COLORS[data] is not False else (0, 0, 0, 255)
        corners = [x + dx, y + dy, x, y + dy, x, y, x + dx, y]
        pyglet.graphics.draw(
            4, pyglet.gl.GL_QUADS, ('v2f', corners), ('c3B', color_rgb * 4)
        )
        # 方块中间数字
        if data != 0:
            a = pyglet.text.Label(text=str(data), bold=True, anchor_x='center',
                                  anchor_y='center', color=(0, 0, 0, 255), x=x + dx / 2, y=y + dy / 2, font_size=28)
            a.draw()

    # 让窗口识别按键
    def on_key_press(self, symbol, modifiers):
        eq_tile = False
        key_press = False
        score = 0
        if symbol == key.UP:
            print('up press')
            self.data, eq_tile, score = self.move_longitudinal(True)
            key_press = True
            # print(self.data)
        elif symbol == key.DOWN:
            print('down press')
            self.data, eq_tile, score = self.move_longitudinal(False)
            key_press = True
        elif symbol == key.RIGHT:
            print('right')
            self.data, eq_tile, score = self.move_crosswise(False)
            print(1)
            key_press = True
            print(self.data)
        elif symbol == key.LEFT:
            print('left')
            self.data, eq_tile, score = self.move_crosswise(True)
            key_press = True
            print(self.data)
        elif symbol == key.ESCAPE:
            self.close()

        score_list = []
        for item in self.data:
            score_list.append(max(item))
        self.score = max(score_list)

        if key_press and (not self.put_tile()):
            # _, a, _ = self.move_crosswise(True)
            # _, b, _ = self.move_crosswise(False)
            # _, c, _ = self.move_longitudinal(False)
            # _, d, _ = self.move_crosswise(True)
            if a and b and c and d:
                print("Game Over")
            """
            a = pyglet.text.Label(text="You Lose, \nPlease try again!", bold=True, anchor_x='center',
                                  anchor_y='center',
                                  color=(255, 255, 205, 255), x=WIN_WIDTH / 2, y=WIN_HEIGHT / 2, width=500,
                                  multiline=True, align='center',
                                  font_size=38, batch=self.main_batch)
            """

    def get_tile_lower_left(self):
        """
        按照宫格的顺序，从左上角方块画起，先获取小方块的左下角
        :return:
        """
        for row in range(WINDOW_BLOCK_NUM):
            for col in range(WINDOW_BLOCK_NUM):
                x = STARTX + BLOCK_WIDTH * col
                y = STARTY + BOARD_WIDTH - BLOCK_WIDTH - BLOCK_WIDTH * row
                self.draw_tile((x, y, BLOCK_WIDTH, BLOCK_WIDTH), self.data[row][col])

    """
    数据核心算法
    """

    def zero_to_end(self, target_list):
        """
            零元素移动到末尾
        :param target_list:
        :return:
        """
        for i in range(-1, -len(target_list) - 1, -1):
            if target_list[i] == 0:
                del target_list[i]
                target_list.append(0)
        return target_list

    def merge_same_number(self, merger_list):
        """
        将数组 相同数字相加
        先将零移至末尾，再合并
        :param merger_list:
        :return:
        """

        merger_list = self.zero_to_end(merger_list)
        for i in range(len(merger_list) - 1):
            if merger_list[i] == merger_list[i + 1]:
                merger_list[i], merger_list[i + 1] = merger_list[i] * 2, 0
                merger_list[:] = self.zero_to_end(merger_list)

        return merger_list

    def move_crosswise(self, bol_crosswise):
        """
        进行左右移动
        :param bol_crosswise: True 左移
        :return:
        """
        oldData = copy.deepcopy(self.data)
        score = 0
        for item in oldData:
            if bol_crosswise:
                item[:] = self.merge_same_number(item)
            else:
                item[::-1] = self.merge_same_number(item[::-1])
        return oldData, oldData == self.data, score

    def transpose_matrix(self, sqr_matrix):
        """
        方阵转置
        :param sqr_matrix:
        :return:
        """
        for c in range(1, len(sqr_matrix)):
            for r in range(c, len(sqr_matrix)):
                sqr_matrix[r][c - 1], sqr_matrix[c - 1][r] = \
                    sqr_matrix[c - 1][r], sqr_matrix[r][c - 1]
        return sqr_matrix

    def move_longitudinal(self, bol_longitudinal):
        """
        进行上下移动
        :param bol_longitudinal:
        :return:
        """

        oldData = copy.deepcopy(self.data)
        print(oldData)
        score = 0
        oldData[:] = self.transpose_matrix(oldData)
        self.data[:] = oldData
        oldData[:], bol, score = self.move_crosswise(True if bol_longitudinal else False)
        oldData[:] = self.transpose_matrix(oldData)
        return oldData, oldData == self.data, score

    def put_tile(self):
        """
        生成随机方块
        :return:
        """
        available = []
        for row in range(WINDOW_BLOCK_NUM):
            for col in range(WINDOW_BLOCK_NUM):
                if self.data[row][col] == 0:
                    available.append((row, col))
        if available:
            row, col = available[random.randint(0, len(available) - 1)]
            self.data[row][col] = 2 if random.randint(0, 1) else 4
            return True
        else:
            return False

    def on_draw(self):
        self.clear()
        self.score_label.text = "Score = %d" % (self.score)
        self.background.draw()
        # self.main_batch.draw()

        #     画小放块 从左上角开始画
        self.get_tile_lower_left()
        self.main_batch.draw()
        self.draw_grid(STARTX, STARTY)


win = Window(WIN_WIDTH, WIN_HEIGHT)

icon = pyglet.image.load('icon.ico')
win.set_icon(icon)
pyglet.app.run()
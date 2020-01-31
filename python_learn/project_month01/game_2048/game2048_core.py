"""
2048    游戏核心算法
"""
"""
1，列表零元素移至末尾
"""
import pyglet

list_merge = [0, 2, 0, 0, 2, 0, 2, 0]


# 对列表修改 从后往前
def zero_to_end():
    """
        零元素移动到末尾
    :param list_merge:
    :return:
    """
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


"""双for写法"""


def zero_to_end_n(list_t):
    for i in range(len(list_t) - 1):
        for c in range(i + 1, len(list_t) - 1):
            if list_t[i] == 0:
                list_t[i], list_t[c] = list_t[c], list_t[i]



# print(list_merge)
"""
将相邻相同数字合并
"""
list01 = [0, 2, 0, 2]


def merge_same_number():
    """
    将数组 相同数字相加
    先将零移至末尾，再合并
    :param list_merger:
    :return:
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i], list_merge[i + 1] = list_merge[i] * 2, 0
            zero_to_end()

# merge_same_number()
# print(list_merge,'111')
"""
第三个 整体向左移动
"""
sqr_matrix = [[2, 4, 2, 2], [4, 0, 2, 2], [2, 4, 0, 4], [0, 0, 2, 2]]


def move_left():
    """
    向左移动
    :param list_source:
    :return:
    """
    global list_merge
    for item in sqr_matrix:
        list_merge = item
        merge_same_number()


move_left()
print(sqr_matrix)


# 向右移动
# 将列表倒置
def move_right():
    global list_merge
    for item in sqr_matrix:
        list_merge = item[::-1]
        merge_same_number()
        # 从右往左接受新列表 合并
        item[::-1] = list_merge


def move_right():
    # global list_merge
    for item in sqr_matrix:
        global list_merge
        list_merge = item[::-1]
        merge_same_number()
        # 从右往左接受新列表 合并
        # 这个其实就是更改列表内元素，依次等于list_merge
        item[::-1] = list_merge


def transpose_matrix(sqr_matrix):
    """
    方阵转置
    :param target_list:
    :return:
    """
    for c in range(1, len(sqr_matrix)):
        for r in range(c, len(sqr_matrix)):
            sqr_matrix[r][c - 1], sqr_matrix[c - 1][r] = \
                sqr_matrix[c - 1][r], sqr_matrix[r][c - 1]


# move_right()

def move_up(sqr_matrix):
    """
    向上移动，转置以后向左
    :return:
    """
    transpose_matrix(sqr_matrix)
    move_left()
    transpose_matrix(sqr_matrix)


def move_down(sqr_matrix):
    """
    往下移动
    :param sqr_matrix:
    :return:
    """
    transpose_matrix(sqr_matrix)
    move_right()
    transpose_matrix(sqr_matrix)

#
# move_up(sqr_matrix)
# print(sqr_matrix)

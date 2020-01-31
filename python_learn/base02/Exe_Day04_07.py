"""
定义方阵转置函数
"""


def transpose_matrix(target_list):
    """
    方阵转置
    :param target_list:
    :return:
    """
    for c in range(1, len(target_list)):
        for r in range(c, len(target_list)):
            target_list[r][c - 1], target_list[c - 1][r] = \
                target_list[c - 1][r], target_list[r][c - 1]


"""
改变外部数据，所以就没有return
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
transpose_matrix(list01)
transpose_matrix(list01)
print(list01)

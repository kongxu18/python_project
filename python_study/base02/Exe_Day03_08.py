"""
矩阵转制
"""
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
a = 0
list02 = []
while a < 4:
    list_temporary = []
    for i in range(len(list01)):
        print(list01[i][a])
        list_temporary.append(list01[i][a])
    list02.append(list_temporary)
    a += 1

print(list02)
'''
更简洁的代码
'''

result = []
for c in range(4):
    result.append([])
    for r in range(4):
        result[c].append(list01[r][c])
print(result)

print(list01)


def change_list(target_list):
    """
    方阵列表转制,计算次数略少于矩阵
    :param target_list:
    :return:
    """
    for x in range(1, len(target_list)):
        for y in range(x, len(target_list)):
            target_list[x - 1][y], target_list[y][x - 1] = target_list[y][x - 1], target_list[x - 1][y]


change_list(list01)
print('--------')
print(list01)

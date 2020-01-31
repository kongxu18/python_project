"""
    算法 ，各种排序 重要的
"""
list01 = [4, 9, 3, 1, 2, 5, 8, 4]


# 冒泡
def bubble(list_):
    # 比较多少轮
    for i in range(len(list_) - 1):
        for j in range(len(list_) - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


# bubble(list01)
print(list01)
"""
    快速排序
"""


def quick(list_, low, high):
    if low < high:
        key = sub_sort(list_, low, high)
        quick(list_, low, key - 1)
        quick(list_, key + 1, high)


def sub_sort(list_, low, high):
    """

    :param list_:
    :param low: 表示列表第一个元素索引
    :param high: 最后一个元素索引
    :return:
    """
    x = list_[low]
    # low向后 high向前
    while low < high:
        # 后面的数往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] = list_[high]
        # 前面的数往前放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]
    list_[low] = x
    return low


# quick(list01, 0, len(list01) - 1)
print(list01)


# 选择排序 就像打擂台
def select(list_):
    # 每轮选出一个最小值
    for i in range(len(list_) - 1):
        # 假设第list【i】为最小值
        min = i
        for j in range(i + 1, len(list_)):
            if list_[min] > list_[j]:
                min = j
        # 交换，将最小值换到应该在的位置
        if min != i:
            list_[i], list_[min] = list_[min], list_[i]


# 插入排序
def insert(list_):
    # 控制每次比较的数是谁，从第二个数开始
    for i in range(1, len(list_)):
        # 空出位置
        x = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > x:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j+1] = x


insert(list01)
print(list01)

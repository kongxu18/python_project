"""
    二分法查找
"""
list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def search(list_, key):
    # 前后索引
    low, high = 0, len(list_) - 1
    while low < high:
        mid = (low + high) // 2
        if list_[mid] < key:
            low = mid + 1
        elif list_[mid] > key:
            high = mid - 1
        else:
            return mid


print(search(list01, 8))

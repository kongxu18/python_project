"""
    阶乘
    递归实现
"""


def fun(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def recursion(num):
    if num <= 1:
        return 1
    return num * recursion(num - 1)

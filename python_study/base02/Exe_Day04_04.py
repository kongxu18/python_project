"""
函数练习
"""


def each_unit_sum(number):
    """
    计算四位数每位数相加
    :param number: 四位整数
    :return:
    """
    result = number % 10 + number // 10 % 10 + \
             number // 100 % 10 + number // 1000
    return result


a = each_unit_sum(1111)
print(a)


def calculate_unit_of_weight(weight: object):
    """
    根据两计算 斤两
    :param weight:
    :return:
    """
    jin = weight // 16
    liang = weight % 16
    dict_unit_of_weight = {'斤': jin, '两': liang}
    # return dict_unit_of_weight
    return jin, liang


a = calculate_unit_of_weight(154)
print(a)


def judge_duplication_oflist(target_list):
    """
    判断列表内重复元素
    :param target_list:
    :return: True：有重复
    """
    for r in range(len(target_list) - 1):
        for c in range(r + 1, len(target_list)):
            if target_list[r] == target_list[c]:
                return True
    return False


list01 = [1, 2, 3, 4, 5, 39]
print(judge_duplication_oflist(list01))

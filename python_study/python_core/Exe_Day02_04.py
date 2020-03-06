"""
练习
    根据年月日，返回星期数
"""
import time


def get_week(year, mon, day):
    dict_weeks = {
        0: '一',
        1: '二',
        2: '三',
        3: '四',
        4: '五',
        5: '六',
        6: '天',
    }
    tuple_time = time.strptime('%d-%d-%d' % (year, mon, day), '%Y-%m-%d')
    result = '新期%s' % dict_weeks[tuple_time.tm_wday]
    return result


a = get_week(2019, 10, 24)
print(a)
"""
    根据出生年月日，计算活了多少天
"""


def get_day(year, mon, day):
    tuple_time = time.strptime('%d-%d-%d' % (year, mon, day), '%Y-%m-%d')
    temp = time.time() - time.mktime(tuple_time)
    print(type(temp))
    result = '结果%.2f' % (temp / 60 / 60 // 34)
    return result


a = get_day(2019, 10, 24)
print(a)

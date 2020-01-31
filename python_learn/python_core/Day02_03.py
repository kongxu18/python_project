"""
    内置模块 时间处理
"""
import time

# 获取当前时间戳，从1970年初到现在经过的秒数
a = time.time()
print(a)
# 2.时间元组(年，月，日，时，分，秒，一周第几天，一年第几天，夏令时)
tuple_time = time.localtime(1571904883.888981)
print(tuple_time)

print(type(tuple_time))

print(tuple_time.tm_year)

# 时间戳 互转 str
a = time.strftime('%Y/%m/%d %H:%M:%S', tuple_time)
print(a)

b = time.strptime(a, '%Y/%m/%d %H:%M:%S')
print(b)

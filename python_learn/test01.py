from typing import List

import pinyin

a = pinyin.get_initial('你好')
print(a[0])

list01 = [[1, 2], [3, 4]]

for item in list01:
    print('---', id(item))
    item = 'a'
    print(id(item))

# for i in range(len(list01)):
#     list01[i]='a'


print(list01)

list02 = [1, 2]
print(list02)
list02 = 'l'
print(list02)

print(''.join(__import__('random').choice('\u2571\u2572') for i in range(50 * 24)))

print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
        x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
"""
这是一个人每到一个地方就会考一次勤，计算总共的考勤时间
"""
import datetime

list_0 = ['08:29:43', '13:13:43', '13:58:00', '14:14:00', '14:31:05', '17:12:13']
temp = []


def string_toDatetime(string):
    return datetime.datetime.strptime(string, '%H:%M:%S')


result = 0  # 总计时间
for i in list_0:
    temp.append(string_toDatetime(i))
    start = temp[0]  # 起始时间
    if len(temp) < 2:
        continue
    end = temp[1]  # 结束时间
    time = (end - start).total_seconds() / 3600  # 每个地方花费时间
    result += time
    print(time)
    temp.clear()

print(result)

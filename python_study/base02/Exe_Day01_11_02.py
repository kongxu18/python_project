# 彩票
import random

lottery_list = []
while len(lottery_list) < 6:
    red_number = random.randint(1, 33)
    if red_number in lottery_list:
        continue
    lottery_list.append(red_number)

lottery_list.sort()
# print(lottery_list)
blue_number = random.randint(1, 16)
lottery_list.append(blue_number)
'''
    # # 疑问这个为何时none
    sort是对 list 进行排序本身没有返回值，所以结果是none
'''
print(lottery_list[0:6])
a=lottery_list[0:6].sort()
print(a)

lottery_list = [str(item) for item in lottery_list]
print(' '.join(lottery_list))


lottery_list02 =[]
red_number01 = input('第一个号:')
while int(red_number01) > 33 or int(red_number01) < 0:
    print('号码不在范围', end='' ' ',)
    red_number01 = input('第一个号:')

lottery_list02.append(red_number01)

red_number02 = input('第二个号:')
while red_number02 in lottery_list02:
    print('号码重复', end='')
    red_number02 = input('第二个号:')

lottery_list02.append(red_number02)

blue_number02 = input('蓝球：')

while len(lottery_list02) < 6:
    red_number = random.randint(1,33)
    if red_number in lottery_list02:
        continue
    lottery_list02.append(red_number)

lottery_list02.append(blue_number)

print(lottery_list02)

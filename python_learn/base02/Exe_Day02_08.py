tuple_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
day_input = input("月 日")
list01 = day_input.split('-')
list01 = [int(x) for x in list01]
day_count = 0
for i in range(list01[0] - 1):
    day_count += tuple_month[i]
day_count += list01[1]
print(day_count)

'''
    使用切片
'''
day_count = 0
day_count = sum(tuple_month[:list01[0] - 1]) + list01[1]
print(day_count)
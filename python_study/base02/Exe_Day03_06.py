''' 对列表进行排序 '''
list_test = [3, 80, 45, 5, 7, 1]

for i in range(len(list_test) - 1):
    # number01 = list_test[i]
    for index in range(i + 1, len(list_test)):
        # 第一个数需要实时的变动，列表每次改变，第一个数也跟着需要改变
        number01 = list_test[i]
        number02 = list_test[index]
        if number01 > number02:
            list_test[i], list_test[index] = number02, number01

print(list_test)

list01 = [3, 80, 45, 1, 80, 5]
result = False
for i in range(len(list01) - 1):
    for index in range(i + 1, len(list01)):
        number01 = list01[i]
        number02 = list01[index]
        if number01 == number02:
            print(number01)
            result = True
            break
if result == False:
    print(list01)

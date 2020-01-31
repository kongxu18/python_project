input2 = '11'
# input = input('二次')
print(pow(2.12, 3))

a = '23'
int(a)

# print(type(a))


message = '齐天大肾是什么'
print(message[0:5:])
print(message[-1:-4:-1])
print(message[2:4])
# 使用切片获取元素会创建一个新列表
list01 = [1, 23, 4]
list02 = list01[:]
list01[0] = 100
print(id(list02), id(list01))

print('=========')
list01 = [1, 2, 3]
list02 = list01
list01[0] = 'asd'
print(list02[0])

print((1, 2, 3) < (1, 4))
print({1, 2, 3} < {1, 4})

d = dict([('a', 1), ('n', 2)])
print(d)

print('---------')

list01 = [[1, 2, 3], [1, 2], [2, 3]]
ceshi = []


def fun01():
    for i in list01:
        ceshi = i


fun01()
print(ceshi)

print('-----------')
"""疑问"""
list01 = [[1, 2, 3], [1, 2], [2, 3]]

list02 = list01[:]
list02[1].append(99)

list_merge = []
for item in list01:
    # item[0:2] = [1, 3, 4]
    list_merge = item[::-1]
    item= list_merge

print(item,'----l')

for i in range(len(list01)):
    list01[i] = list01[i][::-1]

print(list01)
# print(list02)

print('------------')
a = [1,2]
b = a
b = a.append(3)
print(a)

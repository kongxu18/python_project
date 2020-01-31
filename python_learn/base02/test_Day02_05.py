# 列表创建预留空间内存测试
'''

id 没有改变啊 已解决
'''

list01 = []
print(id(list01))
list01.insert(1, 1)
list01.insert(1, 2)
list01.insert(1, 3)
list01.insert(1, 4)
list01.insert(1, 5)
list01.insert(2, 6)
print(id(list01))
print(list01)

list01.append(7)
print(id(list01))

print(list01)
print(list01[-2:])
print(list01[5:])

'''
函数测试
'''


def fun01(list01):
    list01[1] = [200]


list01 = [1, [2, 3]]
fun01(list01)
print(list01)

"""
迭代 可迭代对象
"""

# 迭代原理

"""
for 循环原理是什么，可以被for 的原理是什么
    能被for 的对象必须具备 __iter__ 方法
"""
# 获取迭代器
list01 = [1, 2, 3]
iterator = list01.__iter__()
# 循环获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
# 遇到异常停止迭代

"""
练习1 
"""
list01 = ('铁扇公主', '铁锤', '扳手')
iterator01 = list01.__iter__()
while True:
    try:
        item= iterator01.__next__()
        print(item)
    except StopIteration:
        break

"""
字典迭代
"""
dict01={'铁扇公主':100, '铁锤':200, '扳手':300}
iterator02 = dict01.__iter__()
while True:
    try:
        item= iterator02.__next__()
        print(item,dict01[item])
    except StopIteration:
        break

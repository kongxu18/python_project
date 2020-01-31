"""
记录一个函数执行次数
"""
count = 0


def fun01():
    global count
    count += 1


fun01()
fun01()
fun01()
print(count)
"""
09 函数参数
"""


def fun02(a, b, c, d):
    print(a, b, c, d)


# 位置实参 实参与形参的位置依次对应
fun02(1, 2, 3, 4)
# 关键字实参 实参与形参 根据名称进行对应
fun02(b=1, d=2, c=3, a=4)
# 序列实参
"""
星号将序列拆分后按位置与形参进行对应
"""
list01 = ['a', 'b', 'c', 'd']
fun02(*list01)

# 字典实参
dict01 = {'a': 1, 'c': 3, 'd': 4, 'b': 2}
fun02(*dict01.keys())
"""
将字典拆分后按照名称与形参对应
"""
fun02(**dict01)

'''
函数参数 形式参数
'''

# 形参 缺省（默认）参数：如何实参不提供，可以使用默认值
"""
预先给形参值
"""


# 关键字实参+缺省参数 调用者可以随意传递参数
def fun03(a=0, b=0, c=0, d='c'):
    print(a, b, c, d)


fun03(c=1, d=2)

"""练习"""


def time_turn_second(hour=0, minute=0, second=0):
    return hour * 60 * 60 + minute * 60 + second


print(time_turn_second(1, 1))


# 位置形参 默认的
def fun04(a, b, c, d):
    print(a, b, c, d)


# 星号元组形参  将所有实参合并为一个元组
def fun05(*args):
    print(args)


"""
作用 可以让实参个数无限制
一般形参命名为  args
"""

fun05()
fun05('1', None)


# 练习
def sum_total_number(*args):
    return sum(args)


print(sum_total_number(1, 2, 3))


# 命名关键字形参 在星号元组形参以后的位置形参
# 目的 要求实参必须使用关键字实参
def fun06(a, *args, b):
    print(a, args, b)


fun06(2, b=2)


def fun07(*, a, b):
    print(a, b)


fun07(a=1, b=2)


# 双星号字典形参 实参可以传递数量无限的关键字实参
# ** 目的是将实参合并为字典
def fun08(**a):
    print(a)


fun08(a=1, b=2)

"""参数顺序"""


def fun09(a, b, *args, c, d, **kwargs):
    pass


fun09(1, 2, 'a', 'b', c='c', d='d', one=3, two=4, three=5)

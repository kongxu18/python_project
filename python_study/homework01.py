"""
1、	有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。
最后问第一个人，他说是10岁。请问第五个人多大？(递归完成)
"""
list01 = {}


def fun01(age, count=1):
    if count > 5:
        return
    elif count > 1:
        age = age + 2
    list01['第%s' % count] = age
    count += 1
    return fun01(age, count)


fun01(10)
print(list01)

"""
2、	将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""


def prime_number(end=0):
    return [number for number in range(2, end) if check_prime_number(number)]


def check_prime_number(number):
    for item in range(2, number):
        if number % item == 0:
            return False
    return True


print(prime_number(90))
list_prime = prime_number(90)
list_temporary = []


def fun02(number):
    if number in list_temporary:
        return
    for item in list_prime:
        if number % item == 0:
            result = number // item
            list_temporary.append(item)
            return fun02(result)

fun02(90)
print(list_temporary)


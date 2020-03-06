"""
    函数装饰器
    再不改变函数调用以及内部代码情况下，为其添加新功能的函数
"""


def verify_account(func):
    def wapper(*args, **kwargs):
        print('开始验证')
        func(*args, **kwargs)

    return wapper


# 练习：增加验证功能
@verify_account
def deposit(money):
    print('存钱%d' % money)


@verify_account
def withdraw(login_id, pwd):
    print('取钱', login_id, pwd)


deposit(10000)
withdraw('as', 5000)

"""
    再不改变原有功能 调用和定义情况下
    增加新功能，打印函数执行时间
"""
import time


def check_time(func):
    def wapper(*args, **kwargs):
        now_time = time.time()
        func(*args, **kwargs)
        use_time = time.time() - now_time
        print(use_time)

    return wapper


@check_time
def fun01():
    time.sleep(2)
    print('fun01执行完成')


@check_time
def fun02(a):
    time.sleep(1)
    print('fun02执行完成', a)


fun01()
fun02(100)

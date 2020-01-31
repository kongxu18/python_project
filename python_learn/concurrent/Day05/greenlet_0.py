"""
    greenlet 协程 （有点像nodejs 异步）
    协程行为事例
"""
# from greenlet import greenlet
import greenlet


def fun01():
    print('s fun1')
    gr2.switch()
    print('end fun1')
    gr2.switch()


def fun02():
    print('s fun2')
    gr1.switch()
    print('end fun2')


# 将函数变成协程
gr1 = greenlet.greenlet(fun01)
gr2 = greenlet.greenlet(fun02)
# 选择执行哪个协程
gr1.switch()


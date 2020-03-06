"""
    协程 gevent 示例
"""
import gevent

from gevent import monkey

# from time import sleep
# monkey 转化要写在导入相应模块之前
monkey.patch_time()
from time import sleep


# 协程函数
def foo(a, b):
    print('run foo --', a, b)
    sleep(2)
    print('foo again...')


def bar():
    print('run bar --')
    sleep(3)
    print('bar again...')


# 生成协程对象
f = gevent.spawn(foo, 1, 2)
b = gevent.spawn(bar)

# gevent.sleep(5)
# 阻塞等待f，b 两个协程执行完毕
gevent.joinall([f, b])

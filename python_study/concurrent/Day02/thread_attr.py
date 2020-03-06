"""
    线程属性
"""
from threading import Thread
from time import sleep


def fun():
    sleep(3)
    print('线程属性测试')


t = Thread(target=fun, name='tarena')
t.setDaemon(True)
t.start()
# 以下主线程比分之线程早执行完成
# 如果设置 setDaemon 可以设置主线程退出分支随之退出.一般不与join 一起用
t.setName('Tedu')
print('name:', t.getName())
print('isalive', t.is_alive())
print('daemon', t.isDaemon())

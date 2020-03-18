"""
    线程函数传参数
"""
from threading import Thread
from time import sleep


# 含有参数的进程函数
def fun(sec, name):
    print('线程函数')
    sleep(sec)
    print('执行完毕 -- %s' % name)


jobs = []
for i in range(5):
    t = Thread(target=fun, args=(2,), kwargs={'name': 'T%d' % i})
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

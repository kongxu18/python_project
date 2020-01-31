"""
    multiprocessing 参数传递
"""
from multiprocessing import Process
from time import sleep


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print('i am ', name, end=' ')
        print('i am working')


# 按照位置传递给函数
# p = Process(target=worker, args=(2, 'Ben'))
p = Process(target=worker, kwargs={'name': 'ben', 'sec': 2})
p.start()
p.join()

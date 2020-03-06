"""
    进程对象属性
"""
from multiprocessing import Process
from time import sleep
import time


def tm():
    for i in range(3):
        sleep(2)
        print(time.ctime)


p = Process(target=tm, name='进程')
# 进程名称
print('name', p.name)
"""
    必须在start之前设置,
    当设置为True，父进程结束，子进程跟着退出
"""
p.daemon = True

# 对应子进程pid
p.start()
print('pid', p.pid)

# 是否在生命周期
print('is alive', p.is_alive())

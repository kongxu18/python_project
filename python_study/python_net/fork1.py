"""
    fork 创建进程演示2
"""
import os
from time import sleep

print('-----------')
a = 1
pid = os.fork()
if pid < 0:
    print('failed')
#     子进程执行
elif pid == 0:
    sleep(1)
    print('child ', os.getpid())
    print('parent pid', os.getppid())
    # 子进程会复制父进程的所有内存。父进程fork之前开辟的空间子进程同样拥有
    print(a, '--')
    # 这里改变的是子进程的自己的内存空间，不影响父进程内存
    a = 10000
#     父进程执行
else:
    # sleep(1)
    print('child pid --', pid)
    print('parent pid --', os.getpid())
    print('a', a)


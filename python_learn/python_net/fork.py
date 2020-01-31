"""
    fork 创建进程
"""
import os
from time import sleep
pid = os.fork()
if pid < 0:
    print('failed')
#     子进程执行
elif pid == 0:
    sleep(3)
    print('new',pid)
#     父进程执行
else:
    sleep(4)
    print('old',pid)
print('over')

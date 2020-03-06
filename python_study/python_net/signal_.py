"""
    信号处理僵尸

"""
import os, sys
from time import sleep
import signal

"""
    子进程退出时父进程忽略退出行为，子进程由系统处理
"""
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print('-----------')
a = 1
pid = os.fork()
if pid < 0:
    print('failed')
#     子进程执行
elif pid == 0:
    print('child ', os.getpid())
    print('parent pid', os.getppid())
    # 子进程会复制父进程的所有内存。父进程fork之前开辟的空间子进程同样拥有
    # 改变的是子进程的自己的内存空间，不影响父进程内存
    sys.exit(2)
#     父进程执行
else:
    while True:
        pass

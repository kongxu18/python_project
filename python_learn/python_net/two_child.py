"""
    二级子进程处理僵尸进程
    1。父进程创建子进程，等待回收子进程
    2。子进程创建二级子进程然后退出
    3。二级子进程成为孤儿，和原来父进程一同执行事件
"""
import os, sys
from time import sleep


def fun01():
    for i in range(3):
        sleep(2)
        print('写代码')


def fun02():
    for i in range(2):
        sleep(4)
        print('测代码')


pid = os.fork()
if pid < 0:
    print('err')
elif pid == 0:  # 一级子进程
    pid_two = os.fork()
    if pid_two == 0:  # 二级子进程
        fun01()
    else:  # 一级子进程
        os._exit(0)
else:
    # 父进程
    os.wait()  # 此时等待一级子进程退出,由于一级只负责创建二级子进程，阻塞等待的耗时很小
    fun02()

"""
    模拟僵尸进程产生
    子进程先于父进程退出 父进程没有处理子进程的退出状态，此时子进程就会成成为僵尸进程
    父进程退出后，系统会自动回收僵尸进程
"""
import os,sys

pid =os.fork()

if pid<0:
    print('err')
elif pid ==0:
    print('child pid',os.getpid())
    sys.exit('子进程退出')
else:
    """
        os.wait 处理僵尸进程
        阻塞函数，在父进程中阻塞等待处理子进程退出
    """
    pid, status = os.wait()
    print('pid', pid)
    # child 退出状态*256
    print('status', status)
    while True:
        # 父进程不退出
        pass
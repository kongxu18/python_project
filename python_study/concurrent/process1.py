"""
    multiprocessing 模块创建进程
"""
import multiprocessing as mp
from time import sleep

a = 1


def fun():
    """
    进程函数
    :return:
    """
    print('开始一个进程')
    global a
    print('a', a)
    a = 10000
    sleep(5)
    print('end')


p = mp.Process(target=fun)
# 启动进程
p.start()
# 父进程事件
sleep(3)
print('父进程 a', a)
# 回收进程 同样是阻塞的，要等待子进程结束在执行之后的任务。不加join，子进程结束，父进程不结束，产生僵尸进程
p.join()
print('a', a)
"""
pid =os.fork()
if pid == 0:
    fun()
else:
    os.wait()
"""

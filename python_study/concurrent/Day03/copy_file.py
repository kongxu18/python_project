"""
创建2个进程，分别复制一个文件上下部分
"""
from multiprocessing import Process
import os

filename = './timg.jpeg'
size = os.path.getsize(filename)
"""
当把 fr 放在父进程中 ，p1，p2启动顺序变换以后，复制出现问题
父进程创建 fr 两个子进程使用这个 fr会相互影响
"""
fr = open(filename, 'rb')

def top():
    """
    复制上部分
    :return:
    """
    # fr = open(filename, 'rb')
    fw = open('top.jpg', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


def bot():
    """
    复制下半部分
    :return:
    """
    # fr = open(filename, 'rb')
    fw = open('bot.jpg', 'wb')
    # 以开头为基准往后移动 size//2 个字节
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()
# p2.start()
p1.join()
p2.join()

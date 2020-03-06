"""
线程见通信方法 全局变量
    线程协调互斥
    event
"""
from threading import Thread, Event
from time import sleep

# 全局变量用于通信
s = None
# 事件对象
e = Event()


def fun():
    print('前来拜山头')
    global s
    s = '天王盖地虎'
    # 操作完共享资源 e 设置
    e.set()


t = Thread(target=fun)
t.start()
"""
    两种结果都会出现，区别在于主线程和支线程谁先执行
"""
# 人为设置阻塞
e.wait()
print('说对口令自己人')
if s == '天王盖地虎':
    print('宝塔镇河妖', '对咧')
    print('确认过眼神你是对的人')
else:
    print('打死他')

t.join()

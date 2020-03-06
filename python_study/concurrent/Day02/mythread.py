from threading import Thread
from time import *


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        self.target(*self.args, **self.kwargs)


def player(sec, song):
    for i in range(3):
        print('play %s: %s' % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': '凉凉'})

t.start()
t.join()

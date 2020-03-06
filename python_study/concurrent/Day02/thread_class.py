"""
    自定义线程类
"""
from threading import Thread


class ThreadClass(Thread):
    """
    重写父类 init
    """

    def __init__(self, *args, **kwargs):
        self.attr = args[0]
        super().__init__()

    def f1(self):
        print('step 1')

    def f2(self):
        print('step 2')

    def run(self) -> None:
        """
        重写父类方法,覆盖了父类方法
        :return:
        """
        self.f1()
        self.f2()


t = ThreadClass('abc')
t.start()
t.join()

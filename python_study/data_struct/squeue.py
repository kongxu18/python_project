"""
    队列的顺序存储
    思路：1。基于列表完成数据存储
        2。通过封装规定数据操作
"""


class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def enqueue(self, val):
        """
        入队
        :param val:
        :return:
        """
        self._elems.append(val)

    def dequeue(self):
        if not self._elems:
            raise QueueError('empty')
        return self._elems.pop(0)


if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    """
        经典题目 ，队列反转
    """
    from sstack import *
    st=SStack()

    while not sq.is_empty():
        st.push(sq.dequeue())
    while not st.is_empty():
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())

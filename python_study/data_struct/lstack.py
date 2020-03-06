"""
    栈的链式栈
    思路：1。源于链表结构
        2。封装栈的操作方法
        3。用链表的开头作为栈顶 不用每次遍历
"""


class StackError(Exception):
    pass


class Node:
    def __init__(self, val, next=None):
        self.val = val
        # 循环到下一个节点关系
        self.next = next


class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        self._top = Node(val, self._top)

    def pop(self):
        if self._top is None:
            raise StackError('Stack is empty')
        value = self._top.val
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackError('Stack is empty')
        else:
            return self._top.val


if __name__ == '__main__':
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    # if ls._top.next.next.next is None:
    #     print(ls._top.val)
    ls.is_empty()
    print(ls.pop())

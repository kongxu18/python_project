"""
    栈模型的顺序存储
    思路：1。列表即顺序存储，不符合栈的模型特征
        2。利用列表 将其封装，提供接口方法
"""


class StackError(Exception):
    pass


class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶
        self._elems = []

    def is_empty(self):
        """
        判断栈为空
        :return:
        """
        return self._elems == []

    def push(self, val):
        """
        入栈
        :param val:
        :return:
        """
        self._elems.append(val)

    def pop(self):
        """
        出栈
        :return:
        """
        if self.is_empty():
            raise StackError('stack is empty')
        return self._elems.pop()

    def top(self):
        if self.is_empty():
            raise StackError('stack is empty')
        return self._elems[-1]


if __name__ == '__main__':
    # 初始化栈
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())

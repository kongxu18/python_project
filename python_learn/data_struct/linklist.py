"""
    线性表的链式存储
    实现单链表的构建和功能操作
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        # 循环到下一个节点关系
        self.next = next


node1 = Node(1)
node2 = Node(2, node1)
node3 = Node(3, node2)


class LinkList:
    """
        单链表类，生成对象可以进行增删改查操作 线性结构链式存储的简称
        功能 ：可以进行增删改查的操作
        具体操作通过调用具体方法完成
    """

    def __init__(self):
        """
        初始化链表。标记一个链表的开端，以便与获取后续节点
        """
        self.head = Node(None)

    def init_list(self, list_):
        p = self.head
        for item in list_:
            p.next = Node(item)
            p = p.next

    def show(self):
        """
        遍历列表
        :return:
        """
        p = self.head.next
        while p is not None:
            print(p.val)
            # p 向后移动
            p = p.next

    def is_empty(self):
        """
        判断链表为空
        :return:
        """
        if self.head.next is None:
            return False
        else:
            return True

    def clear(self):
        """
        清空链表
        :return:
        """
        self.head.next = None

    def append(self, val):
        """
        尾部插入一个节点
        链表需要遍历到最尾部
        :return:
        """
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def head_insert(self, val):
        """
        头部插入
        :return:
        """
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def insert(self, index, val):
        """
        指定位置插入
        :return:
        """
        p = self.head
        i = 0
        while i < index:
            # 超出位置的最大范围跳出循环
            if p.next is None:
                break
            p = p.next
            i += 1
        node = Node(val)
        node.next = p.next
        p.next = node

    def delete(self, x):
        """
        按值删除
        :param index:
        :return:
        """
        p = self.head
        while p.next and p.next.val != x:
            p = p.next
        if p.next is None:
            raise ValueError('x not in linklist')
        else:
            p.next = p.next.next

    def get_index(self, index):
        """

        :param index:
        :return:
        """
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('index out of range')
            p = p.next
        return p.val


if __name__ == '__main__':
    l = LinkList()
    l.init_list([2, 5, 3, 8, 6])
    # l.head_insert(123)
    # l.insert(1000, 999)
    # l.delete(8)
    print(l.get_index(5), '---')
    l.show()

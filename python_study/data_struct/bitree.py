"""
二叉树的简单实践
    1。使用链式存储，一个node表示一个树的节点
    2。节点考虑使用2个属性变量，分别表示左右连接
                A
         B             C
                D           E
            F       G   I       H
"""
from squeue import *


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的遍历类
class Bitree:
    def __init__(self, root=None):
        """
        传入树根
        :param root:
        """
        self.root = root

    def preorder(self, node):
        """
        先序遍历
        :param node: 根节点
        :return:
        """
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """
        中序排序
        :param node:
        :return:
        """
        if node is None:
            return
        self.inorder(node.left)
        print(node.val, end='')
        self.inorder(node.right)

    #     层次遍历
    def levelorder(self, node):
        """
        利用队列，让初始节点先入队，谁出队就遍历谁，并且
        让它的左右孩子分别入队，直到队列为空
        :param node:
        :return:
        """
        sq = SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            node = sq.dequeue()
            # 打印出队列元素
            print(node.val, end='')
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)


if __name__ == '__main__':
    # 后序排列
    b = Node('b')
    f = Node('f')
    g = Node('g')
    d = Node('d', f, g)
    i = Node('i')
    h = Node('h')
    e = Node('e', i, h)
    c = Node('c', d, e)
    a = Node('a', b, c)
    bt = Bitree(a)
    # bt.preorder(a)
    # bt.inorder(a)
    bt.levelorder(a)

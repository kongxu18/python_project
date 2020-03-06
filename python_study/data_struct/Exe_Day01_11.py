"""
 将2个链式列表按顺序排序合并
"""

from linklist import *

l01 = LinkList()
l01.init_list([1, 2, 3, 5, 7])
l02 = LinkList()
l02.init_list([4, 6])
# l01.show()
l02.show()


def merge(l1, l2):
    # 将l2合并到l1中
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    p.next = q


merge(l01, l02)
l01.show()

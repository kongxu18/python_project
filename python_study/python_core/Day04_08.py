"""
lambda   还没听完
"""


def fun01():
    return 100


a = lambda: 100
re = a()

print(re)

b = lambda p1, p2: p1 > p2
re = b(1, 2)
print(re)

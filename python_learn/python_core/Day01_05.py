"""
运算符重载
"""


class Vector1:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector1(self.x + other)

    def __str__(self):
        return str(self.x)

    def __radd__(self, other):
        return Vector1(self.x + other)

    def __iadd__(self, other):
        self.x += other
        return self


v01 = Vector1(10)
print(v01 + 2)
print(2 + v01)
"""
复合运算符 在原有基础上进行计算
"""
print(id(v01))
# 重写 iadd ，实现原基础上的变化。不然默认add，一般产生新的变化
v01 += 2
print(v01, id(v01))
